from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'core.views.index', name='index'),
    
    url(r'^ajax/subtitles/(?P<file_name>\S+)/$', 'core.views.get_subtitles', name='get_subtitles'),


)
