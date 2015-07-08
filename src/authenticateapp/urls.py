from django.shortcuts import render
from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    # url(r'^$', 'project_name.views.home', name='home'),
    url(r'^', 'authenticateapp.views.login', name='login'),
)
