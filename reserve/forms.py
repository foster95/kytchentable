from django import forms
from .models import Reservation
from menu.models import Allergen
from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator
from django.http import JsonResponse


class ReservationForm(forms.ModelForm):

    """
    Form for guests to create reservations
    """

    guest_phone = forms.CharField(
        max_length=20,
        required=True,
        validators=[
            RegexValidator(
                r'^\+?[0-9\s\-\(\)]{7,20}$',
                "Please enter a valid phone number."
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'tel',
            'pattern': r'^\+?[0-9\s\-\(\)]{7,20}$',
            'title': 'Please enter a valid phone number.',
        })
    )

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
            'guest_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'reservation_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
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
            reservation_datetime = datetime.combine(
                reservation_date,
                datetime.strptime(time_slot, "%H:%M").time()
            )
            reservation_datetime = timezone.make_aware(
                reservation_datetime,
                timezone.get_current_timezone()
            )

            if reservation_datetime < timezone.now():
                raise forms.ValidationError(
                    "You cannot make a reservation in the past."
                )

        return cleaned_data
