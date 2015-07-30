#-*- coding:utf-8 -*-
from django.contrib import admin
from django.db import models
from django import forms
from geeklogistics.news.models import News

class NewsAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    list_display = ('id', 'title', 'ctime', 'utime')    
    ordering = ('-ctime',) #降序

    class Media:
    	js = ('ckeditor/configuration-ckeditor.js', 'ckeditor/ckeditor.js')


admin.site.register(News, NewsAdmin)