from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'core.views.index', name='index'),
    
    #url(r'^area/(?P<area_slug>\S+)$', 'views.view_area', name='view_area'),                        
    url(r'^publicar-vaga/$',      'internships.views.add_internship',       name='add_internship'),   
    url(r'^contato/$',      'core.views.contato',       name='envelope-contact'),   
    url( r'^anunciar-vaga/$', direct_to_template, { 'template': 'companies/companies.html' }),
    
    url(r'', include('social_auth.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    )