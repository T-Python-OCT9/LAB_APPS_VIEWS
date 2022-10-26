from django.urls import path
from . import views

app_name = 'Pages'

urlpatterns = [
    path('home/', views.homePage, name='home')
]