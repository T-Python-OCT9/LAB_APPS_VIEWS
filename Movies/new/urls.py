from django.urls import path 
from . import views

app_name = "new"

urlpatterns = [
    path("home/", views.newHome , name="newhome")
]