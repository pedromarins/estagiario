# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('user_searches.views',    
    url(r'^meus-filtros/$', 'user_search_list'),
    url(r'^meus-filtros/(?P<search_id>\d+)/$', 'user_search_detail'),        
)