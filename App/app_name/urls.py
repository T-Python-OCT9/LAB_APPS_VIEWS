from django.urls import path
from . import views


app_name = "app_name"
urlpatterns = [
    path("home/", views.home, name="home") ,
    path("", views.app_name, name="app_name")
]