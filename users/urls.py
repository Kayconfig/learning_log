"""Defines URL patterns for users"""
from django.urls import path, include
from . import views # similar to from users import views

app_name = 'users' # help django distinguish urls belonging to this app
urlpatterns = [
    #Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    path("register/", views.register, name='register'),
]