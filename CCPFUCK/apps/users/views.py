# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from .models import Banner, Fuckccp
from articles.models import Articles
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class IndexView(View):

    # # 网站首页
    def get(self, request):
        # 取出轮播图
        all_banners = Banner.objects.all().order_by('index')
        all_article = Articles.objects.order_by('-add_time').all()
        banner = Articles.objects.filter(is_banner=True)[:10]
        article_gfw = Articles.objects.order_by('add_time').filter(article_belong='gfw')[:4]
        article_truth = Articles.objects.order_by('add_time').filter(article_belong='truth')[:4]
        article_wumao = Articles.objects.order_by('add_time').filter(article_belong='wumao')[:4]
        article_sin = Articles.objects.order_by('add_time').filter(article_belong='sinccp')[:4]
        article_nanjing = Articles.objects.order_by('add_time').filter(article_belong='nanjmass')[:4]
        out_ccp_num = Fuckccp.objects.all()
        # 使用django-pure-pagination进行分页（https://github.com/jamespacileo/django-pure-pagination）
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 10, request=request)

        articles = p.page(page)
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'banner': banner,
            'all_article': articles,
            'article_gfw': article_gfw,
            'article_truth': article_truth,
            'article_wumao': article_wumao,
            'article_sin': article_sin,
            'article_nanjing': article_nanjing,
            'out_ccp_num': out_ccp_num,
        })


def page_not_found(request):
    out_ccp_num = Fuckccp.objects.all()
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {
        'out_ccp_num': out_ccp_num,
    })
    response.status_code = 404
    return response


def page_error(request):
    out_ccp_num = Fuckccp.objects.all()
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {
        'out_ccp_num': out_ccp_num,
    })
    response.status_code = 500
    return response
