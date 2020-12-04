from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path ("login", views.login,name="login"),
    path ("csignup", views.csignup,name="csignup"),
    path ("fsignup", views.fsignup,name="fsignup"),
    path("verify", views.verify,name="verify"),
    path("signuppath",views.signuppath,name="signuppath"),
]