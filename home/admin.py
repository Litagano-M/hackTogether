from django.contrib import admin
from .models import Hacker

# Register your models here.

admin.site.register(Hacker)

class HackerAdmin(admin.ModelAdmin):
    list_display = ("user", "university_attending")