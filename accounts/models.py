from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upvote=models.IntegerField
    post=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post')
    def __str__(self):
		return self.post

    
