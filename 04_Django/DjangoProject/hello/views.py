from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def rodrigo(request):
	return HttpResponse("Hello, Rodrigo")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

def user(request, username):
    return HttpResponse(f"Hello user, {username}!")