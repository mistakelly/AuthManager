# userauth/urls.py
from django.urls import path
from .views import get_user


urlpatterns = [
    path("users/<str:id>/", get_user, name="get_user"),
]
