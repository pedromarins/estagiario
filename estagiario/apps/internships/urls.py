# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('internships.views',
    url(r'^estagios/$', 'list_internships', name='list_internships'),    
    url(r'^estagios/(?P<state_uf>\w{2})/$', 'list_internships'),
    
    url(r'^(?P<field_slug>\w){6,13}/$', 'list_internships'),        
    url(r'^(?P<field_slug>\w){6,13}/(?P<state_uf>\w{2})/$', 'list_internships'),

    url(r'^estagio/(?P<ins_slug>\w+)/$', 'show_internship'),
    url(r'^estagio/(?P<state_uf>\w{2})/(?P<ins_slug>\w+)/$', 'show_internship'),    
)


