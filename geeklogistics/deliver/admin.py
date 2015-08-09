# -*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.deliver.models import Dispatcher, Driver


class DispatcherAdmin(admin.ModelAdmin):
    list_display = ('id', 'dispatcher_id', 'name', 'phone', 'photo', 'ctime', 'work_status')
    list_filter = ('ctime',)
    search_fields = ('dispatcher_id', 'phone', 'name')
    ordering = ('id',)  # 降序
    readonly_fields = ('ctime', 'status')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'name', 'phone', 'photo', 'ctime', 'work_status')
    list_filter = ('ctime',)
    search_fields = ('driver_id', 'phone', 'name')
    ordering = ('id',)  # 降序
    readonly_fields = ('ctime', 'status')


admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Driver, DriverAdmin)
