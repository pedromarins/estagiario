from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'core.views.index', name='index'),
    
    url(r'', include('internships.urls')),
    url(r'^anunciar-vaga/$',                        'internships.views.add_internship',     name='add_internship'),   
    url(r'^editar-vaga/(?P<internship_id>\d+)/$',   'internships.views.edit_internship',    name='add_internship'),   

    url(r'^contato/$',      'core.views.contato',       name='envelope_contact'),   
    url(r'', include('social_auth.urls')),
    
    url(r'', include('user_searches.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    )


