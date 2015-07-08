from django.shortcuts import render
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns(
    '',
    url(r'^login/$', 'authenticateapp.views.log_in', name='log_in'),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('log_in')},
        name='logout'),
)
