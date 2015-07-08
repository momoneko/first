from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    url(r'^', include('main.urls')),
)
