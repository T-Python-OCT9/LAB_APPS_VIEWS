from django.urls import path
from . import views

name = 'my_app'

urlpatterns = [
    path("home/", views.home, name="home")
]
