from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from iconcessionaris.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concessionaris.views.home', name='home'),
    # url(r'^concessionaris/', include('concessionaris.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', mainpage, name='home'),
	url(r'^clients/(\w+)/order$', clientOrderPage),
	url(r'^login/$', 'django.contrib.auth.views.login'),
)
