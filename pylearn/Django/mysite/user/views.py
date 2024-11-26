from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_protect
# Create your views here.
'''
POST urlencoded: & &
'''
def index(request):
    print(request.method)
    print(request.body)
    # return HttpResponse("Hello, Django!")
    remote_addr = request.META.get('REMOTE_ADDR')
    return render(request,'user/index.html',{'ip':remote_addr})
def form_sub(request):
    return render(request,'user/form.html')
def auth(request):
    #HttpResponse常用的属性
    #return HttpResponse('OK')
    # return HttpResponse('OK',status = 404)#表示请求失败,默认返回200
    # res = HttpResponse('OK')
    # res['user'] = 'wang'#更改响应头
    # res['abc'] = '123'
    # return res

    #JsonResponse 自动转化为json格式并标准化
    # books = {'title':'王尹','price':'20'}
    # return JsonResponse(books)
    print('request.POST:',request.POST)

    #表单跳转到这里,可以用于验证,再重定向
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    if user == 'wangyin' and pwd == '200520':
        return redirect('/user/')
    else:
        #当需要给出一个不一样的页面时,可以换种方式
        # return redirect('/user/form')
        msg = '用户名或密码错误,请重新输入'
        return render(request,'user/form.html',{'msg':msg})#该方法仅适用于静态页面