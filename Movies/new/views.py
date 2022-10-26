from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def newHome (request : HttpRequest):
    # resolve the request
    new_msg = "Hello World, This is my new HOME !"
    return HttpResponse(new_msg)
