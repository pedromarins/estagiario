from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'core.views.index', name='index'),
    

    
    #url(r'^area/(?P<area_slug>\S+)$', 'views.view_area', name='view_area'),                        
    url(r'^anunciar-vaga/$',                        'internships.views.add_internship',     name='add_internship'),   
    url(r'^editar-vaga/(?P<internship_id>\d+)/$',   'internships.views.edit_internship',    name='add_internship'),   



    url(r'^contato/$',      'core.views.contato',       name='envelope_contact'),   
    
    url(r'', include('social_auth.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    )



urlpatterns += patterns('internships.views',
    url(r'^estagios/$', 'list_internships', name='list_internships'),    
    url(r'^estagios/(?P<state_uf>\w{2})/$', 'list_internships'),
    
    url(r'^(?P<field_slug>\w){6,13}/$', 'list_internships'),        
    url(r'^(?P<field_slug>\w){6,13}/(?P<state_uf>\w{2})/$', 'list_internships'),
    
    #url(r'^(?P<field_slug>\w)/(?P<state_uf>\w{2})/$', 'list_internships'),        

    #url(r'^(?P<state_uf>\w{2})/$', 'list_internships'),
    
    #url(r'^(?P<field_slug>\w)/(?P<state_uf>\w{2})/$', 'list_internships'),    

    url(r'^estagio/(?P<ins_slug>\w+)/$', 'show_internship'),
    url(r'^estagio/(?P<state_uf>\w{2})/(?P<ins_slug>\w+)/$', 'show_internship'),

    

    
)

