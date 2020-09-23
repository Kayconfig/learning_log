from django.shortcuts import render,HttpResponse


#homepage
def index(request):
    return HttpResponse("Hello world")
