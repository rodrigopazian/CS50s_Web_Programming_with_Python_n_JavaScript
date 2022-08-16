from socket import fromshare
from django.shortcuts import render
from django import forms

#Global variables
tasks = ["task1", "task2", "task3"]

class SubmmitNewTaskForm(forms.Form):
    task = forms.CharField(label="New Task: ")
    priority = forms.IntegerField(label="Priority: ", max_value=10, min_value=1)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})

def addtask(request):
    return render(request, "tasks/addtask.html", {"form": SubmmitNewTaskForm()})
    