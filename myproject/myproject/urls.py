from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
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

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
