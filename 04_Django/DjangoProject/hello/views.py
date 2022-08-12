from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
#    return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def rodrigo(request):
	return HttpResponse("Hello, Rodrigo")

def greet(request, name):
#   return HttpResponse(f"Hello, {name}!")
    return render(request, "hello/greet.html", {"name": name})

#def user(request, username):
#    return HttpResponse(f"Hello user, {username}!")

