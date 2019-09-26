# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

from mxshop.settings import REGEX_EMAIL, REGEX_MOBILE
from users.models import User, EmailCode, VerifyCode
import re
from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class SmsSerializer(serializers.Serializer):
    """
    短信
    """
    mobile = serializers.CharField(required=True, max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号
        :param mobile:
        :return:
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("此手机号已被注册")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码格式错误")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("请一分钟后再次发送")

        return mobile


class EmailServerSerializer(serializers.Serializer):
    """
    邮件
    """
    email = serializers.CharField(required=True, max_length=50)

    def validate_email(self, email):
        """
        验证邮箱
        :param email:
        :return:
        """
        # 邮箱是否注册
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("此邮箱已被注册")

        # 验证手机号码是否合法
        if not re.match(REGEX_EMAIL, email):
            raise serializers.ValidationError("邮箱格式错误")
        # 验证码发送频率
        three_mintes_ago = datetime.now() - timedelta(hours=0, minutes=3, seconds=0)
        if EmailCode.objects.filter(add_time__gt=three_mintes_ago, email=email).count():
            raise serializers.ValidationError("请三分钟后再次发送")

        return email


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="此用户已存在")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_code(self, code):

        verify_records = EmailCode.objects.filter(email=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            # 判断验证码是否过期
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["email"] = attrs["username"]

        # 将code字段从attrs中删除
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "email", "code", "password")


# class UserRegSerializer(serializers.ModelSerializer):
#     """
#     注册序列化类
#     """
#     code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4,label="验证码",
#                                  error_messages={
#                                      "blank": "请输入验证码",
#                                      "required": "请输入验证码",
#                                      "max_length": "验证码格式错误",
#                                      "min_length": "验证码格式错误"
#                                  },
#                                  help_text="验证码")
#     username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
#                                      validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
#
#     password = serializers.CharField(
#         style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,
#     )
#
#     # def create(self, validated_data):
#     #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
#     #     user.set_password(validated_data["password"])
#     #     user.save()
#     #     return user
#
#     def validate_code(self, code):
#         # try:
#         #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
#         # except VerifyCode.DoesNotExist as e:
#         #     pass
#         # except VerifyCode.MultipleObjectsReturned as e:
#         #     pass
#         verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
#         if verify_records:
#             last_record = verify_records[0]
#
#             five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
#             if five_mintes_ago > last_record.add_time:
#                 raise serializers.ValidationError("验证码过期")
#
#             if last_record.code != code:
#                 raise serializers.ValidationError("验证码错误")
#
#         else:
#             raise serializers.ValidationError("验证码错误")
#
#     def validate(self, attrs):
#         attrs["mobile"] = attrs["username"]
#         del attrs["code"]
#         return attrs
#
#     class Meta:
#         model = User
#         fields = ("username", "code", "mobile", "password")
