from django.http import HttpResponse
from django.shortcuts import render, redirect
from novelapp.models import NovelTag, Art


# Create your views here.
def index(request):


    return render(request, 'novel/books.html',context={"arts": Art.objects.all(), "tags": NovelTag.objects.all()})


def add_tags(request):
    if request.method == 'GET':
        # 新增/?修改
        # 判断是否修改
        id = request.GET.get('id')
        if id:
            tag = NovelTag.objects.get(id=id)
            tag.name = request.POST.get('id')
            return render(request, 'novel/edit_tags.html',{"tag":tag})
        return render(request, 'novel/edit_tags.html')

    else:
        # POST请求
        # 新增?修改
        tag = NovelTag()
        tag.title = request.POST.get('title')
        # 保存到数据库
        tag.save()

        return redirect('/novel/tag_list')  #重定向

def delete_tag(request):
    id = request.GET.get('id')
    if id:
        result = NovelTag.objects.filter(id=id)
        if result.exists():
            result.delete()
        # return redirect('novel/tag_list')
    return redirect('/novel/tag_list')



def tag_list(request):
    print(1)
    return render(request, 'novel/tag_list.html',
                  context={'tags': NovelTag.objects.all()})