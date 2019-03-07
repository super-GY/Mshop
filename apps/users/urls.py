# _*_ coding:utf-8 _*_
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from users.views import UserViewset
router = DefaultRouter()
router.register(r'users', UserViewset, base_name="users")
