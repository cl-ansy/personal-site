from django.views.generic import RedirectView
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'resume.views.home', name='home'),
    url(r'^about/$', 'resume.views.about', name='about'),
    url(r'^resume/$', 'resume.views.resume', name='resume'),
    url(r'^training/$', 'resume.views.training', name='training'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    url(r'^attendance/$', 'attendance.views.attendance', name='attendance'),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # admin panel
    url(r'^csladmin/', include(admin.site.urls)),

    # ;)
    url(r'^admin/$', RedirectView.as_view(url='https://docs.djangoproject.com/en/dev/ref/contrib/admin/')),

    url(r'^eveapps/', include('eveapps.urls')),
)
