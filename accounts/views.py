from allauth.socialaccount.models import SocialAccount
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .admin import Post
from django.core import serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


def Post(request,pk):
    post=Post.objects.get(id=pk)


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







