# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"文章名")
    desc = models.CharField(max_length=800, verbose_name=u"文章描述")
    article_belong = models.CharField(max_length=50, verbose_name=u"类别")
    detail = UEditorField(verbose_name=u"文章内容", width=600, height=300,
                          imagePath="articles/ueditor/", filePath="articles/ueditor/", default='')
    image = models.ImageField(upload_to="article/%Y/%m", verbose_name=u"封面图", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    article = models.ForeignKey(Articles, verbose_name=u"文章", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    times = models.IntegerField(default=0, verbose_name=u"时长(分钟)")
    url = models.CharField(max_length=200, default='', verbose_name=u'访问地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BannerArticle(Articles):
    class Meta:
        verbose_name = '轮播文章'
        verbose_name_plural = verbose_name
        proxy = True
