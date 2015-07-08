from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    # url(r'^$', 'project_name.views.home', name='home'),
    url(r'^$', 'main.views.main_page', name='main'),
)
