from django.urls import path
from . import views


movies ='home'

urlpatterns = [
    path('home/',views.home, name='movies')
]