from django import forms
from .models import Reservation
from menu.models import Allergen
from django.utils import timezone
from datetime import datetime

class ReservationForm(forms.ModelForm):

    """
    Form for guests to create reservations
    """

    allergies = forms.ModelMultipleChoiceField(
            queryset=Allergen.objects.all(),
            required=False,
            widget=forms.CheckboxSelectMultiple()
            )

    class Meta:
        model = Reservation
        fields = [
            'guest_name', 'guest_phone', 'guest_email', 
            'reservation_date', 'time_slot', 'number_of_guests',
            'allergies', 'special_requests'
            ]
        widgets = {
            'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guest_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'guest_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
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