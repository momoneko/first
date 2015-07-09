from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^auth/', include('authenticateapp.urls')),
    url(r'^', include('main.urls')),
)
