from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests', 'special_requests']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(choices=Reservation.TIME_SLOTS),
            'number_of_guests': forms.Select(choices=Reservation.NO_GUESTS),
            'special_requests': forms.Textarea(attrs={'rows': 4}),
        }