from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

#------------------------------------------------------------
#---------First Page if user doesn't write the path ---------
#------------------------------------------------------------
def FirstPage(request: HttpResponse):
    return HttpResponse('You have to write home/ in the path to see the message :) !')


#------------------------------
#--------- Home Page  ---------
#------------------------------
def hello(request: HttpResponse):
    return HttpResponse('Hello World, This is my new HOME !')
