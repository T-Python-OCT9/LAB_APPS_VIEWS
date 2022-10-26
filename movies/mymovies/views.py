from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

def mymovies(request: HttpRequest):
   weclome_msg= "Hello World, This is my new HOME !" 
   return HttpResponse(weclome_msg)