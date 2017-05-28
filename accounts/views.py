from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken, SocialLogin
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from accounts.models import UserProfile
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .admin import Post
from django.core import serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter, fb_complete_login
from rest_auth.registration.views import SocialLoginView



# Log in from Facebook
@csrf_exempt
def mobile_facebook_login(request):
    if request.method=="POST":
        response=HttpResponse
        access_token =str(request.POST['access_token'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                profile=UserProfile.objects.get_or_create(user=user,dp=account.get_avatar_url())
                ser=serializers(profile)
                return Response(ser.data)
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse(str(e))





@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def postFeed(request,format=None):
    post=Post.objects.all()
    x=serializers.serialize('json',post)
    content={'post':x}
    return Response(content)

@csrf_exempt
@api_view(['GET', 'POST', ])
def home(request):
    if request.method=="POST":
        username=str(request.POST['username'])
        passord=str(request.POST['password'])
        user = authenticate(username=username, password=passord)

        if user is not None:
            ser=UserSerializer(user)
            return Response(ser.data)
        else:
            return HttpResponse("wrong id or pass")







