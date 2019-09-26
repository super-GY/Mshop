"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from mxshop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset, IndexCategoryViewset
from operations.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from users.views import UserViewset, EmailViewSet

route = routers.DefaultRouter()

# 用户 url
route.register(r'user', UserViewset, base_name='users')
# 发送邮件 url
route.register(r'email', EmailViewSet, base_name='email')
# 商品 url
route.register(r'goods', GoodsListViewSet, base_name="goods")
# 商品类型 url
route.register(r'categorys', CategoryViewset, base_name="categorys")
# 热词 url
route.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
# 轮播图 url
route.register(r'banners', BannerViewset, base_name="banners")
# 首页商品系列数据 url
route.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")
# 购物车url
route.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
# 订单相关url
route.register(r'orders', OrderViewset, base_name="orders")
# 收藏
route.register(r'userfavs', UserFavViewset, base_name="userfavs")
# 留言
route.register(r'messages', LeavingMessageViewset, base_name="messages")
# 收货地址
route.register(r'address', AddressViewset, base_name="address")

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path(r'', include(route.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口
    url(r'^jwt-auth/', obtain_jwt_token),

    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 指定上传媒体位置

]
