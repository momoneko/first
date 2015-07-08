from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^', include('main.urls')),
    url(r'^auth/', include('authenticateapp.urls')),
)
