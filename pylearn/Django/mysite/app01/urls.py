from django.contrib import admin
from django.urls import path,include
from app01 import views
urlpatterns = [
    path('now',views.now_time)
]