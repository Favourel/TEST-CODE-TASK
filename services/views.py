from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Reservation
from datetime import datetime
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


# Create your views here.


def add_rental_view(request):
    rental_id = datetime.now().timestamp()
    if request.method == "POST":
        form = CreateReservationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if form.checkOut > form.checkIn:
                form.rental_id = rental_id

                try:
                    obj = Reservation.objects.filter(rental_name=form.rental_name).latest("rental_id")
                    form.previous_reservation_id = obj
                    form.save()
                except ObjectDoesNotExist:

                    form.save()
                return redirect("recent_reservation")
            else:
                messages.error(request, "Input a valid date")
                return redirect("add_rental")
    else:
        form = CreateReservationForm()
    context = {
        "form": form
    }
    return render(request, "services/rental.html", context)


def recent_reservation_view(request):
    reservations = Reservation.objects.all()
    context = {
        "reservations": reservations
    }
    return render(request, "services/recent_reservation.html", context)
