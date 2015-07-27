from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
import webapp

admin.autodiscover()

# import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'geeklogistics.views.home', name='home'),
    url(r'^coop/$', 'geeklogistics.views.coop', name='coop'),
    url(r'^poi/apply/$', 'geeklogistics.views.poi_apply', name='poi_apply'),
    url(r'^list/(?P<poi_id>\d+)/$', 'geeklogistics.views.list', name='list'),
    url(r'^intro/$', 'geeklogistics.views.intro', name='intro'),
    url(r'^area/$', 'geeklogistics.views.area', name='area'),
    url(r'^order/$', 'geeklogistics.views.order', name='order'),
    url(r'^api/v1/order/list$', 'geeklogistics.views.order_list', name='order_list'),
    url(r'^order/(?P<deliver_id>\d+)/$', 'geeklogistics.views.order_detail', name='order_detail'),
    url(r'^order/add/$', 'geeklogistics.views.poi_order', name='poi_order'),
    url(r'^custom/$', 'geeklogistics.views.custom', name='custom'),
    url(r'^news/(?P<id>\d+)/$', 'geeklogistics.views.news', name='news' ),
    url(r'^api/v1/poi/login$', 'geeklogistics.views.poi_login', name='poi_login' ),    
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # h5 webapp
    url(r'^m/', include('geeklogistics.webapp.urls')),
    url(r'^m/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.M_MEDIA_SITE})
)
