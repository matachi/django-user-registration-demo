from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import UsernameAvailable

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index', name='index'),
    url(r'^help/$', 'core.views.help', name='help'),
    url(r'^about/$', 'core.views.about', name='about'),
    # url(r'^accountdemo/', include('accountdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('userena.urls')),

    url(r'^api/username_available/(?P<username>[a-zA-Z0-9_-]+)/$', UsernameAvailable.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
