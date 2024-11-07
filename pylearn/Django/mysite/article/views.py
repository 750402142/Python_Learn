from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_article(request,month,year):

    return HttpResponse("%s %s"%(year,month))
