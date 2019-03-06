"""CCPFUCK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users.views import IndexView
from articles.views import GfwArticleListView, TruthArticleListView, WumaoArticleListView, \
    SinccpArticleListView, NanJmassArticleListView, ArticleDetailView
from django.views.static import serve
from settings import MEDIA_ROOT

import xadmin

urlpatterns = [
    url(r'^sinccpxxx0-=/', admin.site.urls),
    url('^$', IndexView.as_view(), name='index'),
    url('^gfw', GfwArticleListView.as_view(), name='gfw'),
    url('^truth', TruthArticleListView.as_view(), name='truth'),
    url('^wumao', WumaoArticleListView.as_view(), name='wumao'),
    url('^sinccp', SinccpArticleListView.as_view(), name='sinccp'),
    url('^nanjmass', NanJmassArticleListView.as_view(), name='nanjmass'),
    url('^ ', ArticleDetailView.as_view(), name=''),
    url(r'^article/', include('articles.urls', namespace='article')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    url(r'ueditor/', include("DjangoUeditor.urls")),
]


handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'