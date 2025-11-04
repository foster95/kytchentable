from django import forms
from .models import Reservation
from menu.models import Allergen

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
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(choices=Reservation.TIME_SLOTS),
            'number_of_guests': forms.Select(choices=Reservation.NO_GUESTS),
            'allergies': forms.CheckboxSelectMultiple(),
            'special_requests': forms.Textarea(attrs={'rows': 4}),
        }