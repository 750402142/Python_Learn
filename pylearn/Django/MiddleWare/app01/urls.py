from django.contrib import admin
from django.urls import path,include
from app01.views import index
urlpatterns = [
    path('',index)
]