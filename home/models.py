from django.db import models
from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipManager

# Create your models here.

class Hacker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    next_hackathon = models.CharField(max_length=100, null=True, blank=True)

class FriendWithMetAtField(Friend):
    objects = FriendshipManager()
    met_at = models.CharField(max_length=100)