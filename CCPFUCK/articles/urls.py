# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from .views import GfwArticleListView, TruthArticleListView, WumaoArticleListView, \
    SinccpArticleListView, NanJmassArticleListView, ArticleDetailView
urlpatterns = [
    # 课程详情页
    url(r'^detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
]
