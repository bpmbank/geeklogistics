from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'geeklogistics.views.home', name='home'),
    url(r'^coop/$', 'geeklogistics.views.coop', name='coop'),
    url(r'^list/$', 'geeklogistics.views.list', name='list'),
    url(r'^intro/$', 'geeklogistics.views.intro', name='intro'),
    url(r'^area/$', 'geeklogistics.views.area', name='area'),
    url(r'^order/$', 'geeklogistics.views.order', name='order'),
    url(r'^custom/$', 'geeklogistics.views.custom', name='custom'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
