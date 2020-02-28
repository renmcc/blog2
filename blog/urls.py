#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/26 2:24
#__author__ = 'ren_mcc'

from django.urls import path
from . import views

urlpatterns = [
    path('blog_title', views.blog_title, name='blog_title'),
    path('<int:article_id>/', views.blog_article, name='blog_article')
]