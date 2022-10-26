from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

def FunHome(request: HttpRequest):
    msg = "Hello World, This is my new HOME !"
    return HttpResponse(msg)