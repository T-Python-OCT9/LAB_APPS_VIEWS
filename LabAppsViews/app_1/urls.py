from django.urls import path
from . import views

app_name = "The_lab_app"

urlpatterns = [
path("", views.Welecom_Page, name="path")
]