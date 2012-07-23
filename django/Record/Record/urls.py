from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'articles.views.index'),
	url(r'^articles/(?P<article_id>\d+)/$', 'articles.views.detail'),
	
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
