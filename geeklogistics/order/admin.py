# -*- coding:utf-8 -*-
from django.contrib import admin
from geeklogistics.order.models import Order


# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

# class OrderResource(resources.ModelResource):

#     class Meta:
#         model = Order

class OrderAdmin(admin.ModelAdmin):
    # resource_class = OrderResource
    list_display = ('id', 'deliver_id', 'poi_name', 'poi_nearest', 'customer_nearest',
                    'order_status', 'status')
    list_filter = ('ctime',)
    search_fields = ('order_id', 'deliver_id')  # 刷新浏览器，你会在页面顶端看到一个查询栏。 添加了一个根据姓名查询的查询框。
    ordering = ('-order_id',)  # 降序
    readonly_fields = ('ctime', 'status')

    def start_time_format(self, instance):
        return instance.start_time.strftime("%d %b %Y %H:%M:%S")

    def dstatus(self, instance):
        st = instance.get_status_display()
        return st

    dstatus.short_description = '订单删除状态'

    def poi_name(self, instance):
        if not instance.poi is None:
            link = '<a href="">' + instance.poi.name + '</a>'
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
