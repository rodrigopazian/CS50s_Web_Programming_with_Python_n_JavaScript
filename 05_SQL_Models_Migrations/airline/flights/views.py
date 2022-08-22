from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {"flight": flight, "passengers": flight.passengers.all(), "non_passengers": Passenger.objects.exclude(passengerflights=flight).all()})

def book(request, flight_id):
    if request.method == "POST":
        flightid = Flight.objects.get(pk=flight_id)
        passengerid = Passenger.objects.get(pk=int(request.POST["passengerid"]))
        passengerid.passengerflights.add(flightid)
        return HttpResponseRedirect(reverse("flights:flight", args=(flightid.id,)))
        