from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("apply/",apply,name="apply"),
    path("accounts/login/",login,name="login"),
    path("accounts/logout/",logout,name="logout"),
    path("applied_students/",applied_students , name="applied_students")
]
