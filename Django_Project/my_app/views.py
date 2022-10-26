# Create your views here.
from django.shortcuts import render


from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest):
    # resolve the request
    massege = "Hello World, This is my new HOME !"
    return HttpResponse(massege)
