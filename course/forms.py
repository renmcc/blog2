#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/3/2 17:56
#__author__ = 'ren_mcc'
from django import forms
from .models import Course

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title","overview")

