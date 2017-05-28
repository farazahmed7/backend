from __future__ import unicode_literals
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from stream_django.activity import Activity

from django.db import models



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=100)

    def __str__(self):
        return self.post

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    dp=models.CharField(max_length=100)
    fullName=models.CharField(max_length=100)
    def __str__(self):
        return self.user.get_full_name()