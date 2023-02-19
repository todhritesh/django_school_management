from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("apply/",apply,name="apply"),
    path("accounts/login/",login,name="login"),
    path("accounts/logout/",logout,name="logout"),
    path("applied_students/",applied_students , name="applied_students"),
    path("student_details/<int:id>",student_details , name="student_details"),
    path("approve/<int:id>",approve , name="approve"),
    path("edit/<int:id>",edit , name="edit"),
    path("delete/<int:id>",delete , name="delete"),
    path("class",manage_class , name="manage_class"),
]
