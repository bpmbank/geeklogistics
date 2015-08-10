# -*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.poi.models import Merchant, Show


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'tel')
    list_filter = ('ctime',)
    search_fields = ('name', 'tel')  # 刷新浏览器，你会在页面顶端看到一个查询栏。 添加了一个根据姓名查询的查询框。
    ordering = ('id',)  # 降序
    readonly_fields = ('ctime',)


class ShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'poi_name', 'position')

    def poi_name(self, instance):
        return instance.poi.name

    poi_name.short_description = '商家'


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Show, ShowAdmin)
