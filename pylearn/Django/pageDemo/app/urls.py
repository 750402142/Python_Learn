from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add, name='add'),

    path("page/", views.page),

    path('page2/', views.page2),
]
