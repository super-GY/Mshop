# _*_ coding:utf-8 _*_
from django.db.models import Q
from rest_framework import serializers
from goods.models import GoodsCategory
from goods.models import GoodsImage, Goods, HotSearchWords, Banner, GoodsCategoryBrand, IndexAd

__author__ = "super.gyk"


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化类
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    """
    商品轮播图序列化类
    """

    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    """
    商品 序列化类
    """
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class HotWordsSerializer(serializers.ModelSerializer):
    """
    热搜词 序列化类
    """

    class Meta:
        model = HotSearchWords
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    """
    轮播的商品 序列化类
    """

    class Meta:
        model = Banner
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    """
    品牌名 序列化类
    """

    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"


class IndexCategorySerializer(serializers.ModelSerializer):
    """
    首页商品类别广告 序列化类
    """
    brands = BrandSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id, )
        if ad_goods:
            good_ins = ad_goods[0].goods
            goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
            category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"
