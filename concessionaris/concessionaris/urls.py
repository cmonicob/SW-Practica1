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
    url(r'^clients/(\w+)/$', clientInfoPage),
    url(r'^clients/(\w+)/orders$', clientOrderPage),
    
    # Car Dealers pages
    url(r'^cardealers/$',carDealersListPage),
    url(r'^cardealers/(\w+)/$', carDealersInfoPage),
    url(r'^cardealers/(\w+)/orders$', carDealersOrderPage),
    url(r'^cardealers/(\w+)/create$', carDealersCreate.asView(), name="carDealersCreate"),
    url(r'^cardealers/(\w+)/edit$', carDealersEdit),
    url(r'^cardealers/(\w+)/delete$', carDealersDelete),
    # Brands pages
    url(r'^brands/$',brandsListPage),
    url(r'^brands/(\w+)/$', brandsInfoPage),
    url(r'^brands/(\w+)/create$', brandsCreate),
    url(r'^brands/(\w+)/edit$', brandsEdit),
    url(r'^brands/(\w+)/delete$', brandsDelete),
    # Orders pages
    url(r'^orders/(\w+)/$', ordersInfoPage), 
    url(r'^orders/(\w+)/create$', ordersCreate),
    url(r'^orders/(\w+)/edit$', ordersEdit),
    url(r'^orders/(\w+)/delete$', ordersDelete),
    

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', user_logout),
)
