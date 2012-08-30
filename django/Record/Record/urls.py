from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'articles.views.index'),
	url(r'^articles/(?P<article_slug>[\w\-]+)/$', 'articles.views.detail'),
	url(r'^sections/(?P<section>[\w\-]+)/$', 'articles.views.section'),

	url(r'^archive/latest/$', 'issues.views.latest'),
	url(r'^archive/$', 'issues.views.archive'),
	url(r'^archive/(?P<volume>\d+)/(?P<issue>\d+)/$', 'issues.views.detail'),

	(r'^search/', include('haystack.urls')),
)

urlpatterns += staticfiles_urlpatterns()
