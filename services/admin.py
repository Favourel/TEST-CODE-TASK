from django.contrib import admin
from .models import *

# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["rental_name", "rental_id", "checkIn", "checkOut", "previous_reservation_id"]


admin.site.register(Rental)
admin.site.register(Reservation, ReservationAdmin)
