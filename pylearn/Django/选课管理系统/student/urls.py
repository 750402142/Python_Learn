from django.contrib import admin
from django.urls import path, include,re_path
from student import views
urlpatterns = [

    path('index',views.index),

    path('register',views.register),
    path('form',views.form),
    path('add',views.add),
    re_path('delete/(\d+)',views.delete),
    re_path('edit/(\d+)',views.edit),
    path('elective',views.elective),
    path('search',views.search)

]