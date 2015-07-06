from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import hello, helloWorld, current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', helloWorld),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
)
