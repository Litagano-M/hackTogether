from django.db import models
from django.contrib.auth.models import User
from friendship.models import Friend


# Create your models here.

class Hacker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university_attending = models.CharField(max_length=100)
