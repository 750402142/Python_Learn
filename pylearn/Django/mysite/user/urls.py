from operator import index

from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include,register_converter
from user import views
urlpatterns = [
    path('',views.index),
    path('form',views.form_sub),
    path('auth',views.auth)
]