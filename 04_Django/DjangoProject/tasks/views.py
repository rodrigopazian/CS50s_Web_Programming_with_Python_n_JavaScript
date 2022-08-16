from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

#Global variables
tasks = []

class SubmmitNewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", max_value=5, min_value=1)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})

def addtask(request):
    if request.method == "POST":
        form = SubmmitNewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            # return HttpResponseRedirect("/tasks")
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/addtask.html", {"form": form})
    return render(request, "tasks/addtask.html", {"form": SubmmitNewTaskForm()})
    