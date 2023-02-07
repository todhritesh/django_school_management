from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("apply/",apply,name="apply"),
    path("about/",about,name="about"),
]
