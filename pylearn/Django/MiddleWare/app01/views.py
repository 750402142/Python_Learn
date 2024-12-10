from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return HttpResponse('<h3>这是h3标签</h3>')