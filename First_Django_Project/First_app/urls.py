from django.urls import path, include
from . import views

name_app = "First_App"

urlpatterns = [
    path('', views.welcome_page, name = "home"),
]
