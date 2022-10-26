from django.urls import path
from . import views



app_name = "FirstApp"

urlpatterns = [
path("home/", views.home, name="home")
]
