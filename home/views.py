from django.shortcuts import render
from .models import FriendWithMetAtField

# Create your views here.

def home(request):
    friends_of_user = FriendWithMetAtField.objects.friends(request.user)
    return render(request, "index.html", context={"friends": friends_of_user})