from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("login", views.login, name='home'),
    path("home", views.home, name='home'),
    path("forg", views.forg, name='home')
]   