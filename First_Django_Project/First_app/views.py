from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def welcome_page(request: HttpRequest):
    welcome_msg = "Hello World, This is my new HOME !"
    return HttpResponse(welcome_msg)