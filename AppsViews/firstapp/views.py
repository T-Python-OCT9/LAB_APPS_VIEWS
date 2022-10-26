from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
app_name = 'home'

def masseage(request: HttpRequest):
    masseage_text = 'Hello World, This is my new HOME !'
    return HttpResponse(masseage_text)
