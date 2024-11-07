from django.contrib import admin
from django.urls import path, include, re_path
from article import views
urlpatterns = [
    re_path("(?P<year>\d{4})/(?P<month>\d{1,2})",views.get_article)
]