#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
import webapp

admin.autodiscover()

# import views

urlpatterns = patterns('',
    # pc页面相关:
    url(r'^$', 'geeklogistics.views.home', name='home'),
    url(r'^coop/$', 'geeklogistics.views.coop', name='coop'),
    url(r'^poi/apply/$', 'geeklogistics.views.poi_apply', name='poi_apply'),
    url(r'^list/(?P<poi_id>\d+)/$', 'geeklogistics.views.list', name='list'),
    url(r'^intro/$', 'geeklogistics.views.intro', name='intro'),
    url(r'^area/$', 'geeklogistics.views.area', name='area'),
    url(r'^order/$', 'geeklogistics.views.order', name='order'),
    url(r'^order/(?P<deliver_id>\d+)/$', 'geeklogistics.views.order_detail', name='order_detail'),
    url(r'^order/add/$', 'geeklogistics.views.poi_order', name='poi_order'),
    url(r'^order/success/(?P<deliver_id>\d+)/$', 'geeklogistics.views.order_success', name='order_success'),
    url(r'^custom/$', 'geeklogistics.views.custom', name='custom'),
    url(r'^news/(?P<id>\d+)/$', 'geeklogistics.views.news', name='news' ),
    url(r'^app/$', 'geeklogistics.views.app', name='app' ),

    # 订单相关 
    url(r'^order/import$', 'geeklogistics.order.views.import_order', name='import_order'),

    # 分拣站相关
    url(r'^api/v1/station/login$', 'geeklogistics.station.views.login', name='station_login'),
    url(r'^station/list/(?P<station_id>\d+)/$', 'geeklogistics.station.views.order_list', name='order_list'),

    # 配送员相关
    url(r'^api/v1/dispatcher/login$', 'geeklogistics.deliver.views.dispatcher_login', name='dispatcher_login'),
    url(r'^api/v1/driver/login$', 'geeklogistics.deliver.views.driver_login', name='driver_login'),

    # api相关
    url(r'^api/v1/order/list$', 'geeklogistics.order.views.order_list', name='order_list'),
    url(r'^api/v1/order/add$', 'geeklogistics.order.views.order_new', name='order_new' ),
    url(r'^api/v1/order/updateStatus$', 'geeklogistics.order.views.update_order_status', name='update_order_status'), 
    url(r'^api/v1/order/delete$', 'geeklogistics.order.views.order_delete', name='order_delete'), 
    url(r'^api/v1/order/detail$', 'geeklogistics.order.views.order_detail_ajax', name='order_detail_ajax' ),    
    url(r'^api/v1/poi/login$', 'geeklogistics.poi.views.poi_login', name='poi_login' ),  


    url(r'^admin/', include(admin.site.urls)),

    # h5 webapp
    url(r'^m/', include('geeklogistics.webapp.urls')),
    url(r'^m/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.M_MEDIA_SITE})
)
