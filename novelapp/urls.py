
from django.contrib import admin
from django.urls import path

import novelapp
from novelapp import views
app_name = "novelapp"
urlpatterns = [
    # 声明主页面的请求
    path('', views.index),
    # path
]
