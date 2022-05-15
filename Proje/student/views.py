from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. This is fscohort index page.")

def henry(request):
    return HttpResponse("Henry")

def kral(request):
    return HttpResponse("Kral")