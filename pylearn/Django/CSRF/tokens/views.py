from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.middleware.csrf import get_token
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = {"login": False, "msg": "用户名或密码错误"}
        if username == 'wangyin' and password == "200520":
            res["login"] = True
            res["msg"] = ""
        return JsonResponse(res)
    else:
        return render(request, 'login.html')
# def token_sure(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     res = {"login":False,"tokens":"111"}
#     if username == 'wangyin' and password == "200520":
#         res["login"] = True
#         res["tokens"] = "登录成功"
#
#     return JsonResponse(res)

def get_tokens(request):
    token = get_token(request)
    print(token)
    return HttpResponse(token)
def index(request):

    return render(request,'index.html')