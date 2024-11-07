from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def index(request):
    print(request.method)
    print(request.POST )
    return HttpResponse("Hello, Django!")
def form_sub(request):
    return render(request,'user/form.html')
def auth(request):
    print(request.POST)
    return HttpResponse('OK')