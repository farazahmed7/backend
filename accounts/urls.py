from django.conf.urls import url, patterns
from . import views
from startup import settings



urlpatterns = [
    url(r'^api/$', views.home, name='home'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))