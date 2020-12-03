from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path ("login", views.login,name="login"),
    path ("signup", views.signup,name="signup"),
    path("verify", views.verify,name="verify"),

]