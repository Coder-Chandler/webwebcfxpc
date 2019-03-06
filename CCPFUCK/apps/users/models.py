#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default=u"", verbose_name=u"昵称")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), default="female", max_length=6)
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=100, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Fuckccp(models.Model):
    out_ccp_num = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = u"退党人数"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.out_ccp_num