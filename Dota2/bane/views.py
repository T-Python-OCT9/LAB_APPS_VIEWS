from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 


def Dota2_Name(request : HttpRequest) :
    welcome_msg = "Hello World, This is my new HOME !"
 
    return HttpResponse(welcome_msg)

# Create your views here.
