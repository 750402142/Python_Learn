"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include,register_converter
from app01 import views


# 定义路由转发器
class MobileConverter(object):
    regex = '1[3-9]\d{9}'
    def to_python(self,value):
        return value
register_converter(MobileConverter,'mobile')#生成的参数可以在其他地方同样调用

urlpatterns = [

    # 路由分发
    #路由分发的执行顺序为先根据'time/'来判断在哪个app中,然后到对应的app指向文件中得到完整的path(),正确执行

    path('time/',include('app01.urls')),

    path('article/',include('article.urls')),

    # 路由转发,其目的是让不用在path里面写上负责的正则匹配过程
    path('phone/<mobile:mobile>',views.test),

    path('user/',include('user.urls'))
]