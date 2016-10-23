from django.conf.urls import url, patterns, include
from . import views,feeds
from startup import settings



urlpatterns = [
    url(r'^api/$', views.home, name='home'),
    url(r'^feed/$',views.postFeed,name='feed'),
     url(r'^f/$',feeds.RssFeed(),name='Post'),
    url(r'^login/$', views.mobile_facebook_login, name='mobile_facebook_login'),

    url(r'^accounts/', include('allauth.urls')),


]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))