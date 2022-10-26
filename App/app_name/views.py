from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse ,HttpRequest
def app_name(request: HttpRequest):
    return HttpResponse("This page displays information about the movies")
