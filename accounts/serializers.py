from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('dp','fullName')
