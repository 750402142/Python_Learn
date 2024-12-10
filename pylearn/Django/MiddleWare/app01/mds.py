from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponse
class mid(MiddlewareMixin):

    def process_request(self, request):

        # print(request.META.get('REMOTE_ADDR'))#该请求得到的ip
        #用来判断非法ip
        if request.META.get('REMOTE_ADDR') == '127.0.0.1':
            return HttpResponse("<h3>这是一个非法ip</h3>")#返回不是None时,会进行拦截,从当前往回执行
        return None #当返回None意味着没有任何问题
    def process_response(self, request, response):
        #request 请求函数的请求体
        #response 视图函数的响应体
        print(response.content)#被拦截时得到的是request的return返回的
        return response
