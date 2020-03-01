#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/29 21:34
#__author__ = 'ren_mcc'
from django import template
from django.db.models import Count
from article.models import ArticlePost
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
    return user.article.count()

@register.inclusion_tag("article/list/latest_articles.html")
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {'latest_articles': latest_articles}

@register.simple_tag
def most_commented_articles(n=3):
    # annotate 给queryset加一个注释
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]

@register.filter(name='markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))
