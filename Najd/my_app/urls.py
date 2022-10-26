from django.urls import path
from . import views

my_app='app1'

urlpatterns=[
    path("" , views.home ,name="home")
]