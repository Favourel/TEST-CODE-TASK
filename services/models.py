from django.db import models
from django.conf import settings
# from datetime import datetime

# Create your models here.


class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental_name = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='rental_service')
    rental_id = models.CharField(max_length=20, null=True, blank=True)
    checkIn = models.DateField()
    checkOut = models.DateField()
    previous_reservation_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.rental_id}"
