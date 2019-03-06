# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from .models import Articles
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from users.models import Fuckccp


class GfwArticleListView(View):
    def get(self, request):
        all_article = Articles.objects.order_by('-add_time').filter(article_belong='gfw')
        out_ccp_num = Fuckccp.objects.all()
        # 使用django-pure-pagination进行分页（https://github.com/jamespacileo/django-pure-pagination）
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 10, request=request)

        article = p.page(page)

        return render(request, 'gfw.html', {
            'all_article': article,
            'out_ccp_num': out_ccp_num,
        })


class TruthArticleListView(View):
    def get(self, request):
        all_article = Articles.objects.filter(article_belong='truth').order_by('-add_time')
        out_ccp_num = Fuckccp.objects.all()

        # 使用django-pure-pagination对课程进行分页（https://github.com/jamespacileo/django-pure-pagination）
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 10, request=request)

        article = p.page(page)

        return render(request, 'truth.html', {
            'all_article': article,
            'out_ccp_num': out_ccp_num,
        })


class WumaoArticleListView(View):
    def get(self, request):
        all_article = Articles.objects.filter(article_belong='wumao').order_by('-add_time')
        out_ccp_num = Fuckccp.objects.all()

        # 使用django-pure-pagination对课程进行分页（https://github.com/jamespacileo/django-pure-pagination）
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 10, request=request)

        article = p.page(page)

        return render(request, 'wumao.html', {
            'all_article': article,
            'out_ccp_num': out_ccp_num,
        })


class SinccpArticleListView(View):
    def get(self, request):
        all_article = Articles.objects.filter(article_belong='sinccp').order_by('-add_time')
        out_ccp_num = Fuckccp.objects.all()

        # 使用django-pure-pagination对课程进行分页（https://github.com/jamespacileo/django-pure-pagination）
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 10, request=request)

        article = p.page(page)

        return render(request, 'sinccp.html', {
            'all_article': article,
            'out_ccp_num': out_ccp_num,
        })


class NanJmassArticleListView(View):
    def get(self, request):
        all_article = Articles.objects.filter(article_belong='nanjmass').order_by('-add_time')
        out_ccp_num = Fuckccp.objects.all()

        # 使用django-pure-pagination对课程进行分页（https://github.com/jamespacileo/django-pure-pagination）
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 10, request=request)

        article = p.page(page)

        return render(request, 'nanjmass.html', {
            'all_article': article,
            'out_ccp_num': out_ccp_num,
        })


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = Articles.objects.get(id=int(article_id))
        out_ccp_num = Fuckccp.objects.all()
        return render(request, 'article_detail.html', {
            'article': article,
            'out_ccp_num': out_ccp_num,
        })
