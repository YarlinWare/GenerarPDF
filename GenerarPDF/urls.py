from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'GenerarPDF.views.home', name='home'),
                       url(r'^', include('clientes.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
