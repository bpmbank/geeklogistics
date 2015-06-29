#-*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ctime', 'utime')    
    ordering = ('-ctime',) #降序

admin.site.register(News, NewsAdmin)