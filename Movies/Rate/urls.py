from django.urls import path
from . import views

app_name = "Rate"

urlpatterns = [ path("home/", views.home, name="home") ]