from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path ("", views.login,name="login"),
    path ("csignup", views.csignup,name="csignup"),
    path ("fsignup", views.fsignup,name="fsignup"),
    path("cverify", views.cverify,name="cverify"),
    path("fverify", views.fverify,name="fverify"),
    path("signuppath",views.signuppath,name="signuppath"),
    path("login",views.login,name="login"),
    path("forget_password",views.forget_password,name="forget_password"),
    path("change_password", views.change_password,name="change_password"),


]