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
    
    # ----------- api pages -----------
    url(r'^$', mainpage, name='home'),
    # Clients pages
    url(r'^clients/$',clientListPage),
    #url(r'^clients/(\w+)/$', clientInfoPage),
    url(r'^clients/(\w+)/order$', clientOrderPage),
    # Car Dealers pages
    #url(r'^cardealers/$',carDealersListPage),
    #url(r'^cardealers/(\w+)/$', carDealersInfoPage),
    #url(r'^cardealers/(\w+)/order$', carDealersOrderPage),
    # Brands pages
    #url(r'^brands/$',brandsListPage),
    #url(r'^brands/(\w+)/$', brandsInfoPage),
    # Orders pages
    #url(r'^orders/(\w+)/$', ordersInfoPage),
    # 
    url(r'^login/$', 'django.contrib.auth.views.login'),
)
