#-*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.deliver.models import Dispatcher

class DispatcherAdmin(admin.ModelAdmin):
    list_display = ('id', 'dispatcher_id', 'name', 'current_location', 'phone', 'photo', 'ctime', 'status')
    list_filter = ('ctime',) 
    search_fields = ('dispatcher_id', 'phone', 'name')
    ordering = ('id',) #降序

admin.site.register(Dispatcher, DispatcherAdmin)