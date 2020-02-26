#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/26 13:33
#__author__ = 'ren_mcc'

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        #哪些表单数据写入字段
        fields = ('username', 'email')

    #调用is_valid()时会被执行
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords do not match.')
        return cd['password2']

#注册自定义字段
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')

#个人信息类
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school","company","profession","address","aboutme","photo")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)