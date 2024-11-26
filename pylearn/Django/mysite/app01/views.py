import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.

def now_time(request):
    time_str = datetime.datetime.now().strftime('%H:%m:%d %X')
    # 其中第一个参数request是默认的,第二个参数表示templates下的文件,第三个参数,前者是文件中的占位参数,后者是函数中生成的参数
    return render(request, 'time_now.html', {'now': time_str})
def converter(request,mobile):
    print('mobile',)
    return HttpResponse(mobile)
def test(request,m):
    return render(request,'converter.html',{'phone':m})
