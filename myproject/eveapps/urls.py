from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'eveapps.views.eveapp_index', name='eveapp_index'),
    url(r'^testappone/$', 'eveapps.views.testappone', name='testappone'),
    url(r'^testapptwo/$', 'eveapps.views.testapptwo', name='testapptwo'),
)
