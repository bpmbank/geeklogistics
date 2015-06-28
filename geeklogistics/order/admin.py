#-*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'deliver_id', 'current_location')
    list_filter = ('ctime',) 
    search_fields = ('order_id', 'deliver_id') #刷新浏览器，你会在页面顶端看到一个查询栏。 添加了一个根据姓名查询的查询框。
    ordering = ('-order_id',) #降序

admin.site.register(Order, OrderAdmin)