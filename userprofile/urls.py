from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_profile_view, name="myprofile"),
    url(r'^(?P<id>\d+)', views.profile_view, name="profile"),
]