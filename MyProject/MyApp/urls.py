from django.urls import path
from . import views

app_name = "MyApp"

urlpatterns = [
   path("home/", views.home, name="home")
]

