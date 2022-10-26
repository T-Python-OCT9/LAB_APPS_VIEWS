from django.urls import path
from . import views

app_name = "My_First_WebSite"

urlpatterns = [
path("home/", views.Dota2_Name, name="home")
]
