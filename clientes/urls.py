__author__ = 'archi'
from django.conf.urls import patterns, include, url
from clientes import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', views.IndexView.as_view(), name='home'),
                       url(r'^generar_pdf/$', views.generar_pdf, name='pdf'),
                       )
