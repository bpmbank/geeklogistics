from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'geeklogistics.webapp.views.home', name='home'),
                       url(r'^intro/$', 'geeklogistics.webapp.views.intro', name='intro'),
                       url(r'^service/$', 'geeklogistics.webapp.views.service', name='service'),
                       url(r'^contact/$', 'geeklogistics.webapp.views.contact', name='contact'),
                       url(r'^news/$', 'geeklogistics.webapp.views.news', name='news'),
                       url(r'^order/search/$', 'geeklogistics.webapp.views.order_search', name='order_search'),
                       url(r'^order/(?P<deliver_id>\d+)/$', 'geeklogistics.webapp.views.order_result',
                           name='order_result'),
                       url(r'^merchant/login/$', 'geeklogistics.webapp.views.merchant_login', name='merchant_login'),
                       url(r'^dispatcher/login/$', 'geeklogistics.webapp.views.dispatcher_login',
                           name='dispatcher_login'),
                       url(r'^list/(?P<dispatcher_id>\d+)/$', 'geeklogistics.webapp.views.dispatcher_orders',
                           name='dispatcher_orders'),
                       url(r'^location/update$', 'geeklogistics.webapp.views.location_update', name='location_update'),

                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
