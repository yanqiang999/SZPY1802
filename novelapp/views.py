from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #     请求路径和请求方法
    print(request.path, request.method)
    # 请求头的元信息和GET请求参数, 查询参数
    print(request.META, request.GET)
    # POST请求参数,表单参数
    print(request.POST)
    # return HttpResponse("<h1>你好!<h1/>")

    return render(request, 'novel/books.html',context={"name":"天龙八部", "author":"金庸"})