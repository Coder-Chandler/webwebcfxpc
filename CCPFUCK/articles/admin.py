from django.contrib import admin
from .models import Articles, Video
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'article_belong', 'detail', 'image', 'add_time', 'is_banner']
    search_fields = ['name', 'desc', 'article_belong', 'detail']
    list_filter = ['name', 'desc', 'article_belong', 'detail', 'image', 'add_time', 'is_banner']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'times', 'url', 'add_time']
    search_fields = ['article', 'name', 'url']
    list_filter = ['article', 'name', 'times', 'url', 'add_time']


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Video, VideoAdmin)
