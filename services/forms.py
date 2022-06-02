from django import forms
from .models import *

choices = Rental.objects.all().values_list("name", "name")
choice_list = []

for item in choices:
    choice_list.append(item)


class CreateReservationForm(forms.ModelForm):
    rental_name = forms.Select(attrs={"class": 'form-control', "placeholder": "Select Rental Service"}, choices=choices)

    checkIn = forms.DateTimeField(widget=forms.TextInput(attrs={

        'type': 'date',
        'name': 'checkIn',
        'id': 'checkIn',
        'class': 'form-control'
    }
    )
    )
    checkOut = forms.DateTimeField(widget=forms.TextInput(attrs={
        'type': 'date',
        'name': 'checkOut',
        'id': 'checkOut',
        'class': 'form-control'
    }
    )
    )

    class Meta:
        model = Reservation
        fields = ["rental_name", "checkIn", "checkOut"]

