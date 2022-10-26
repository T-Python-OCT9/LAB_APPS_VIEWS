from django.urls import path
from . import views

app_name = "my_first_app"
urlpatterns =[ path('home/', views.home, name="home")]