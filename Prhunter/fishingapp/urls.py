from django.urls import URLPattern, path
from . import views

app_name = "prhunter"

urlpatterns = [
    path ("home/" , views.home , name= "home")]