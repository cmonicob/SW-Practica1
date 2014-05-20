from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from iconcessionaris.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    # Clients pages
    url(r'^clients/$',clientListPage.as_view(), name='client_list'),
    url(r'^clients/(?P<pk>\d+)/$', clientDetail.as_view(), name='client_detail'),
    url(r'^clients/(?P<pk>\d+)/orders$', clientOrderPage.as_view(), name='clientOrder_list'),
    url(r'^clients/create$',clientCreate.as_view(), name='client_create'),	
    url(r'^clients/(?P<pk>\d+)/edit$', clientEdit.as_view(), name='client_edit'),
#    url(r'^clients/(?P<pk>\d+)/delete$', clientDelete),
    # Car Dealers pages
    url(r'^cardealers/$',carDealersListPage.as_view(), name='carDealer_list'),
    url(r'^cardealers/(?P<pk>\d+)/$', carDealersInfoPage.as_view(), name='carDealer_detail'),
    url(r'^cardealers/(?P<pk>\d+)/orders$', carDealersOrdersListPage.as_view(), name='order_list'),
    url(r'^cardealers/(?P<pk>\d+)/orders/create$', carDealersOrderCreate.as_view(), name='order_create'),
    url(r'^cardealers/create$', cardealersCreate.as_view(), name='carDealer_create'),
#    url(r'^cardealers/(?P<pk>\d+)/edit$', carDealersEdit),
#    url(r'^cardealers/(?P<pk>\d+)/delete$', carDealersDelete),
    # Brands pages
    url(r'^brands/$',brandsListPage.as_view(), name='brand_list'),
    url(r'^brands/(?P<pk>\d+)/$', brandsDetail.as_view(), name='brand_detail'),
    url(r'^brands/create$', brandsCreate.as_view(), name='brand_create'),
#    url(r'^brands/(?P<pk>\d+)/edit$', brandsEdit),
#    url(r'^brands/(?P<pk>\d+)/delete$', brandsDelete),
    # Orders pages
    url(r'^orders/(?P<pk>\d+)/$', ordersDetail.as_view(), name='order_detail'),
#    url(r'^orders/(?P<pk>\d+)/edit$', ordersEdit),
#    url(r'^orders/(?P<pk>\d+)/delete$', ordersDelete),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', user_logout),
)
