from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request : HttpRequest):
    welcome_msg = "Welcome to the biggest Movies Database in the world !"
    return HttpResponse(welcome_msg)
