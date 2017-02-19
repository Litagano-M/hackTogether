from django.contrib import admin
from .models import Hacker, FriendWithMetAtField

# Register your models here.

admin.site.register(Hacker)
admin.site.register(FriendWithMetAtField)

class HackerAdmin(admin.ModelAdmin):
    list_display = ("user", "university")