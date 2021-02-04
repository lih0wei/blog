from django.http import HttpResponse
from django.shortcuts import render
from cache.models import *
# Create your views here.
from django.core.cache import caches
#装饰器
cacheobj = caches['default']
def cache_wrapper(func):
    def _wrapper(request,*args,**kwargs):
        #从缓存中读取数据
        data = cacheobj.get(request.path)

        #判断获取的数据是否存在缓存中
        if data:
            print('读取缓存中的数据')
            return HttpResponse(data)
        #执行views函数从数据库中获取数据
        print('从数据中获取数据')
        response = func(request,*args,**kwargs)

        #将数据库中查询的数据存入缓存
        cacheobj.set(request.path,response.content)
        return response

    return _wrapper

@cache_wrapper
def index_view(request):
    clist = Clazz.objects.all()
    return render(request,'indexn.html',{'clist':clist})