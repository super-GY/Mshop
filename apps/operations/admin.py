#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    """
    用户收藏
    """
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(object):
    """
    用户留言
    """
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(object):
    """
    收货地址
    """
    list_display = ["signer_name", "signer_mobile", "district", "address"]


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
