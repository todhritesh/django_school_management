from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("apply/",apply,name="apply"),
    path("login/",login,name="login"),
]
