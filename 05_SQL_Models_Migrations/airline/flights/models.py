from tkinter import CASCADE
from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__ (self):
        return f"{self.code} -- {self.city}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__ (self):
        return f"{self.id} : {self.origin} to {self.destination}"

class Passenger(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    passengerflights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__ (self):
        return f"{self.firstname} {self.lastname}"
