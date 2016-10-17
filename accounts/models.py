from __future__ import unicode_literals
from django.contrib.auth.models import User
from stream_django.activity import Activity

from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)


class Post(models.Model,Activity):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote = models.IntegerField
    post = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.post