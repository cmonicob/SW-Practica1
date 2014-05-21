from django.conf.urls import patterns, include, url
from django.conf import settings

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
    url(r'^clients/(?P<pk>\d+)/delete$', clientDelete.as_view(), name='client_delete'),
    # Car Dealers pages
    url(r'^cardealers/$',carDealersListPage.as_view(), name='carDealer_list'),
    url(r'^cardealers/(?P<pk>\d+)/$', carDealersInfoPage.as_view(), name='carDealer_detail'),
    url(r'^cardealers/(?P<pk>\d+)/orders$', carDealersOrdersListPage.as_view(), name='order_list'),
    url(r'^cardealers/create$', carDealersCreate.as_view(), name='carDealer_create'),
    url(r'^cardealers/(?P<pk>\d+)/edit$', carDealersEdit.as_view(), name='carDealer_edit'),
    url(r'^cardealers/(?P<pk>\d+)/delete$', carDealersDelete.as_view(), name='carDealer_delete'),
    # Brands pages
    url(r'^brands/$',brandsListPage.as_view(), name='brand_list'),
    url(r'^brands/(?P<pk>\d+)/$', brandsDetail.as_view(), name='brand_detail'),
    url(r'^brands/create$', brandsCreate.as_view(), name='brand_create'),
    url(r'^brands/(?P<pk>\d+)/edit$', brandsEdit.as_view(), name='brand_edit'),
    url(r'^brands/(?P<pk>\d+)/delete$', brandsDelete.as_view(), name='brand_delete'),
    # Orders pages
    url(r'^orders/(?P<pk>\d+)/$', ordersDetail.as_view(), name='order_detail'),
    url(r'^orders/(?P<pk>\d+)/edit$', ordersEdit.as_view(), name='order_edit'),
    url(r'^orders/create$', ordersCreate.as_view(), name='order_create'),
    url(r'^orders/(?P<pk>\d+)/delete$', ordersDelete.as_view(), name='order_delete'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', user_logout),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.STATIC_ROOT, }),
	)
