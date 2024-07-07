# userauth/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import registeruser
from .views import loginuser


urlpatterns = [
    path("register/", registeruser, name="authenticate_user"),
    path("login/", loginuser, name="authenticate_user"),
]
