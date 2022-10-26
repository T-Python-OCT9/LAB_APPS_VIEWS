from django.urls import path
from . import views

app_name = "mymovies"

urlpatterns = [

path("",views.mymovies , name="home")

]