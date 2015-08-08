#-*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.station.models import Station

class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone','latitude', 'longitude', 'station_type')
    list_filter = ('ctime',) 
    search_fields = ('name', 'phone') #刷新浏览器，你会在页面顶端看到一个查询栏。 添加了一个根据姓名查询的查询框。
    ordering = ('id',) #降序

admin.site.register(Station, StationAdmin)