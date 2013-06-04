# -*- coding: utf-8 -*-

from django.conf.urls import *
from space.views import *
from django.contrib import admin
from django.contrib.auth.views import login,logout

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
	(r'^index/$',index),
	(r'^intro/$',intro),
    (r'^events/$',events),
    (r'^service/$',service),
    (r'^support/$',business_support),
    (r'^about_us/$',about_us),
    (r'^contact_form/$',contact),
    (r'^search_form/$',search_form),
    (r'^search/$',search),
    (r'download/application_form/$',download_application_form),
    (r'accounts/login/$',login),
    (r'accounts/logout/$',logout),
    (r'register/$',register),
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
