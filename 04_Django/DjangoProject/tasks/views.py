from socket import fromshare
from django.shortcuts import render
from django import forms

#Global variables
tasks = ["task1", "task2", "task3"]

class SubmmitNewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", max_value=5, min_value=1)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})

def addtask(request):
    if request.method == "POST":
        form = SubmmitNewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/addtask.html", {"form": form})
    return render(request, "tasks/addtask.html", {"form": SubmmitNewTaskForm()})
    