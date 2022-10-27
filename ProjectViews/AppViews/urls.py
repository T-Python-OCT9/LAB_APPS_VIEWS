from django.urls import path     
from . import views

app_name = 'AppViews'

urlpatterns = [
    path('', views.FirstPage , name= 'FirstPage' ),
    path('home/', views.hello , name='home')
]