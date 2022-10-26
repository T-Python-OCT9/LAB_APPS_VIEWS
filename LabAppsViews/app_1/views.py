from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def Welecom_Page(request : HttpResponse):
  return HttpResponse("Hello World, This is my new HOME !")

