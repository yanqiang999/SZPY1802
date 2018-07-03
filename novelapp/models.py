from django.db import models

# Create your models here.

class NovelTag(models.Model):
    title = models.CharField(max_length=20,verbose_name="作品类别",unique=True)
    add_time = models.DateTimeField(verbose_name="添加时间",auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="作品类别",auto_now=True)


# 小说文章模型
class Art(models.Model):
    title = models.CharField(max_length=50, unique=True,verbose_name='文章名')
    # 作者模型,建立多对一的关联
    author = models.CharField(max_length=20, blank=True,verbose_name='作者')
    summary = models.TextField(verbose_name='概述')
    # img_url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='', verbose_name="封面")
    counter = models.IntegerField(default=0, verbose_name="阅读次数")
    publish_time = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")

#     文章类型
    tag = models.ForeignKey(NovelTag, on_delete=models.SET_NULL, null=True)

