#-*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.order.models import Order
from geeklogistics.poi.models import Merchant


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'dispatcher_name', 'poi_name', 
        'start_time', 'order_status')
    list_filter = ('ctime',) 
    search_fields = ('order_id', 'deliver_id') #刷新浏览器，你会在页面顶端看到一个查询栏。 添加了一个根据姓名查询的查询框。
    ordering = ('-order_id',) #降序
    readonly_fields = ('ctime', 'status')

    def start_time_format(self, instance):
        return instance.start_time.strftime("%d %b %Y %H:%M:%S")

    def poi_name(self, instance):
        if not instance.poi is None:
            link = '<a href="">'+instance.poi.name+'</a>'
        else:
            link = ''
    	# return instance.poi.name
        return link
    poi_name.allow_tags = True
    poi_name.short_description = '订单商家'

    def dispatcher_name(self, instance):
        if not instance.dispatcher is None:
    	   return instance.dispatcher.name
        else:
            return ''
    dispatcher_name.short_description = '配送员'


    def station_name(self, instance):
        if not instance.current_location is None:
    	   return instance.current_location.name
        else:
            return ''
    station_name.short_description = '当前配送位置'

admin.site.register(Order, OrderAdmin)

