from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Reservation
from datetime import datetime
from .forms import *

# Create your views here.


def home_view(request):
    context = {

    }
    return render(request, "services/home.html", context)


def add_rental_view(request):
    rental_id = datetime.now().timestamp()
    if request.method == "POST":
        form = CreateReservationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.rental_id = rental_id
            prev = Reservation.objects.filter(rental_name=form.rental_name).last()
            if prev.exists():
                # Reservation.objects.filter(previous_reservation_id=form.rental_id).last()
                prevv = Reservation.objects.filter(rental_name=form.rental_name,
                                                    rental_id=form.rental_id).last()
                form.previous_reservation_id = prevv
                form.save()
            else:
                # previous_reservation_id = Reservation.objects.filter(rental_id=form.rental_id).last()
                # form.previous_reservation_id = previous_reservation_id
                form.save()
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
