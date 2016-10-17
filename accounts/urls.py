from django.conf.urls import url, patterns, include
from . import views,feeds
from accounts.views import FacebookLogin
from startup import settings



urlpatterns = [
    url(r'^api/$', views.home, name='home'),
    url(r'^feed/$',views.postFeed,name='feed'),
     url(r'^f/$',feeds.RssFeed(),name='Post'),
     url(r'^f1$', views.Post, name = 'Post'),
    url(r'^accounts/', include('allauth.urls')),
     url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),


]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))