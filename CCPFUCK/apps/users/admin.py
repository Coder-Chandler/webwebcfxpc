# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import UserProfile, Banner, Fuckccp
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['nick_name', 'birthday', 'gender', 'address', 'mobile']
    search_fields = ['nick_name', 'address', 'mobile']
    list_filter = ['nick_name', 'birthday', 'gender', 'address', 'mobile']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

class OutNum(admin.ModelAdmin):
    list_display = ['out_ccp_num']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Fuckccp, OutNum)
