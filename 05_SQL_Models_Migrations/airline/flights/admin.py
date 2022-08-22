from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightCustomView(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerCustomView(admin.ModelAdmin):
    filter_horizontal = ("passengerflights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightCustomView)
admin.site.register(Passenger, PassengerCustomView)
