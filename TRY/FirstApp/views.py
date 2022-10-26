from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

def home(request:HttpRequest):
    
    welcoming="Hello World, This is my new HOME !" 
    return HttpResponse(welcoming)

