from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request : HttpRequest):
    # resolve the request
    welcome= "Hello World, This is my new HOME !"
    return HttpResponse(welcome)