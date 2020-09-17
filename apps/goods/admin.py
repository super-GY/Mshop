#!/usr/bin/env python
# encoding: utf-8


import xadmin
from .models import Goods, Category, GoodsImage, GoodsBrand, Banner, HotSearchWords
from .models import IndexAd


class GoodsAdmin(object):
    """
    商品
    """
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "ueditor"}

    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodsCategoryAdmin(object):
    """
    商品类别
    """
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class GoodsCategoryBrandAdmin(object):
    """
    商品品牌
    """
    list_display = ["category", "image", "name", "desc", "add_time"]

    def get_context(self):
        context = super(GoodsCategoryBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = Category.objects.filter(category_type=1)
        return context


class BannerAdmin(object):
    """
    轮播商品
    """
    list_display = ["goods", "image", "index"]


class HotSearchWordsAdmin(object):
    """
    热搜词
    """
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(object):
    """
    首页商品类别广告
    """
    list_display = ["category", "goods"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Category, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(GoodsBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(HotSearchWords, HotSearchWordsAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)

