from django.urls import URLPattern ,path
from . import views

app_name = "firstapp"

urlpatterns = [
    path("home/", views.masseage, name="home")
]

