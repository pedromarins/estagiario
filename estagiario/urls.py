from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'core.views.index', name='index'),
    
    url(r'^contato/$',      'core.views.contato',       name='envelope-contact'),   
    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    )