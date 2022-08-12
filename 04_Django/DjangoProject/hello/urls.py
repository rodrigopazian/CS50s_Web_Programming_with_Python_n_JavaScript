from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rodrigo", views.rodrigo, name="rodrigo"),
    #path("<str:name>", views.greet, name="greet"),
    path("<str:username>", views.user, name="user")
]