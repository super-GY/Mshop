# _*_ coding:utf-8 _*_
# from django.conf.urls import url
# from rest_framework.routers import DefaultRouter
#
# from users.views import UserViewset

"""
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
from django.urls import path
from rest_framework import routers

from users import views

route = routers.DefaultRouter()
route.register(r'user', views.UserViewset, base_name='users')

urlpatterns = [
    path('user/', views.UserViewset, name='user'),
    path('email/', views.EmailViewSet, name='email'),

]

