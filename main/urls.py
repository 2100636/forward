# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from main.views import *


urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^sozdanie-saitov/$', SaitView.as_view(), name='sait'),
    url(r'^mobilnie-prilojeniya/$', MobileView.as_view(), name='mobile'),
    url(r'^prodvijenie/$', ProdvijenieView.as_view(), name='prodvijenie')
)
