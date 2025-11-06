from django import forms
from .models import Reservation
from menu.models import Allergen
from django.utils import timezone
from datetime import datetime

class ReservationForm(forms.ModelForm):
    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergen.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests', 'allergies', 'special_requests']
        widgets = {
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
