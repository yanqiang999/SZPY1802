from django.conf.urls import url
from django.contrib import admin


import novelapp
from novelapp import views

urlpatterns = [
    # 声明主页面的请求
    url(r'^tags',views.add_tags,name='tags'),
    url(r'^tag_list',views.tag_list,name='tag_list'),
    # url(r'^tag_list',views.tag_list),
    url(r'^delete_tag',views.delete_tag,name='delete_tag'),
    url('', views.index),

    # path
]
