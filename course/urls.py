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
    path('create-course/', views.CreateCourseView.as_view(), name='create_course'),
    path('delete-course/<int:pk>', views.DeleteCourseView.as_view(), name='delete_course'),
    path('create-lesson/', views.CreateLessonView.as_view(), name='create_lesson'),
    path('list-lessons/<int:course_id>/', views.ListLessonsView.as_view(), name='list_lessons'),
    path('detail-lesson/<int:lesson_id>/',views.DetailLessonView.as_view(), name='detail_lesson'),
]