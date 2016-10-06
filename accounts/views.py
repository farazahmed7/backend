from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.

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



