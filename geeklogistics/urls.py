from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'geeklogistics.views.home', name='home'),
    url(r'^coop/$', 'geeklogistics.views.coop', name='coop'),
    url(r'^list/(?P<poi_id>\d+)/$', 'geeklogistics.views.list', name='list'),
    url(r'^intro/$', 'geeklogistics.views.intro', name='intro'),
    url(r'^area/$', 'geeklogistics.views.area', name='area'),
    url(r'^order/$', 'geeklogistics.views.order', name='order'),
    url(r'^order/(?P<deliver_id>\d+)/$', 'geeklogistics.views.order_detail', name='order_detail'),
    url(r'^custom/$', 'geeklogistics.views.custom', name='custom'),
    url(r'^news/(?P<id>\d+)/$', 'geeklogistics.views.news', name='news' ),
    url(r'^user/login/$', 'geeklogistics.views.poi_login', name='poi_login' ),

    

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
