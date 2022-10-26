from django.urls import path
from . import views

app_name = "App1"

urlpatterns = [
path("", views.home, name="home")
]