from django.urls import path
from . import views

app_name="Book"

urlpatterns =[
    path("Book/",views.home,name="Book")
]