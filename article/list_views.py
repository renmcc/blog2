#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/28 19:16
#__author__ = 'ren_mcc'
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import ArticlePost


def article_titles(request, username=None):
    '''
    文章首页显示摘要
    :param request:
    :return:
    '''
    if username:
        user = User.objects.get(username=username)
        articles_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        articles_title = ArticlePost.objects.all()
    paginator = Paginator(articles_title, 4)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    if username:
        return render(request, "article/list/author_articles.html", {"articles":articles,"page": current_page, "userinfo":userinfo,"user":user})
    return render(request, "article/list/article_titles.html", {"articles":articles,"page": current_page})

def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, "article/list/article_content.html", {"article":article})

@csrf_exempt
@require_POST
@login_required()
def like_article(request):
    '''
    点赞方法
    :param request:
    :return:
    '''
    article_id = request.POST.get('id')
    action =request.POST.get('action')
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == 'like':
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except Exception as e:
            print(e)
            return HttpResponse('no')