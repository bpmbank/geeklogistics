#-*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.poi.models import Merchant

class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'tel')
    list_filter = ('ctime',) 
    search_fields = ('name', 'tel') #刷新浏览器，你会在页面顶端看到一个查询栏。 添加了一个根据姓名查询的查询框。
    ordering = ('id',) #降序

admin.site.register(Merchant, MerchantAdmin)