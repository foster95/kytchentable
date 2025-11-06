from django import forms
from .models import Reservation
from menu.models import Allergen
from django.utils import timezone
from datetime import datetime
import re

class ReservationForm(forms.ModelForm):
    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergen.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Reservation
        fields = ['guest_name', 'guest_phone', 'guest_email', 'reservation_date', 'time_slot', 'number_of_guests', 'allergies', 'special_requests']
        widgets = {
            'guest_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Full name',
                    'required': True,
            }),
            'guest_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
                'required': True,
            }),
            'guest_phone': forms.TextInput(attrs={
                'type': 'tel',
                'class': 'form-control',
                'placeholder': '+44 7123 456789',
                'pattern': '^(\\+44\\s?7\\d{3}\\s?\\d{6}|07\\d{3}\\s?\\d{6})$',
                'title': 'Enter a valid UK phone number, e.g. +44 7123 456789 or 07123 456789',
                'required': True,
                }),
            'reservation_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': timezone.localdate().strftime('%Y-%m-%d')  # prevents selecting past dates
                }
            ),
            'time_slot': forms.Select(choices=Reservation.TIME_SLOTS),
            'number_of_guests': forms.Select(choices=Reservation.NO_GUESTS),
            'allergies': forms.CheckboxSelectMultiple(),
            'special_requests': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        """
        Prevent reservations in the past (including earlier today).
        """
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        time_slot = cleaned_data.get('time_slot')

        if reservation_date and time_slot:
            # Combine date and time into a single datetime
            reservation_datetime = datetime.combine(
                reservation_date,
                datetime.strptime(time_slot, "%H:%M").time()
            )
            reservation_datetime = timezone.make_aware(reservation_datetime, timezone.get_current_timezone())

            # Compare to current datetime
            if reservation_datetime < timezone.now():
                raise forms.ValidationError("You cannot make a reservation in the past.")

        return cleaned_data