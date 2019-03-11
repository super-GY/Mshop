"""Mshop URL Configuration

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

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset, IndexCategoryViewset
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
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(route.urls)),

]
