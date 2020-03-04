#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/3/1 22:40
#__author__ = 'ren_mcc'
from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('course-list/', views.CourseListView.as_view(), name='course_list'),
    path('manage-course/', views.ManageCourseListView.as_view(), name='manage_course'),
]