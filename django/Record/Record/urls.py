from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'articles.views.index'),
	url(r'^articles/(?P<article_id>\d+)/$', 'articles.views.detail'),
	
)

urlpatterns += staticfiles_urlpatterns()
