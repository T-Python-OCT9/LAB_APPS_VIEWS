from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request : HttpRequest):

    wl_mg = 'Not Hello World, This is my new HOME !'

    return HttpResponse(wl_mg)