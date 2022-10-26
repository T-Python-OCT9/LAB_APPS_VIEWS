from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def homePage(request: HttpResponse):
    welcome_message = 'Hello World, This is my new HOME !'
    return HttpResponse(welcome_message)

# Create your views here.
