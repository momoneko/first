from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    # url(r'^$', 'project_name.views.home', name='home'),
    url(r'^private2/$', 'main.views.private2', name='private2'),
    url(r'^private/$', 'main.views.private', name='private'),
    url(r'^$', 'main.views.main_page', name='main'),
)
