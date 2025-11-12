from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from menu.models import Allergen
from django.core.exceptions import ValidationError
from datetime import datetime
from django.core.validators import RegexValidator


# Create your models here.

"""
Model to store reservation details.

"""


class Reservation(models.Model):

    # Options for number of guests from 1 to 7
    NO_GUESTS = [(i, str(i)) for i in range(1, 7)]

    TIME_SLOTS = [
        ('10:00', '10:00'),
        ('10:15', '10:15'),
        ('10:30', '10:30'),
        ('10:45', '10:45'),
        ('11:00', '11:00'),
        ('11:15', '11:15'),
        ('11:30', '11:30'),
        ('11:45', '11:45'),
        ('12:00', '12:00'),
        ('12:15', '12:15'),
        ('12:30', '12:30'),
        ('12:45', '12:45'),
        ('13:00', '13:00'),
        ('13:15', '13:15'),
        ('13:30', '13:30'),
        ('13:45', '13:45'),
        ('14:00', '14:00'),
        ('14:15', '14:15'),
        ('14:30', '14:30'),
        ('14:45', '14:45'),
        ('15:00', '15:00'),
        ('15:15', '15:15'),
        ('15:30', '15:30'),
        ('15:45', '15:45'),
        ('16:00', '16:00'),
        ('16:15', '16:15'),
        ('16:30', '16:30'),
        ('16:45', '16:45'),
        ('17:00', '17:00'),
        ('17:15', '17:15'),
        ('17:30', '17:30'),
        ('17:45', '17:45'),
        ('18:00', '18:00'),
        ('18:15', '18:15'),
        ('18:30', '18:30'),
        ('18:45', '18:45'),
        ('19:00', '19:00'),
        ('19:15', '19:15'),
        ('19:30', '19:30'),
        ('19:45', '19:45'),
        ('20:00', '20:00'),
        ('20:15', '20:15'),
        ('20:30', '20:30'),
        ('20:45', '20:45'),
        ('21:00', '21:00'),
        ('21:00', '21:00'),
        ('21:30', '21:00'),
        ('21:45', '21:45'),
        ('22:00', '22:00'),
        ('22:15', '22:15'),
    ]

    MAXIMUM_TABLES = 15

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, blank=True, null=True)
    guest_phone = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                r'^\+?[0-9\s\-\(\)]{7,20}$',
                "Please enter a valid phone number"
                ),
            ],
        )

    guest_email = models.EmailField(max_length=254, blank=True, null=True)
    reservation_date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)
    number_of_guests = models.PositiveIntegerField(choices=NO_GUESTS)
    allergies = models.ManyToManyField(Allergen, blank=True)
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['reservation_date', 'time_slot']

    def __str__(self):
        return (
            f"Reservation for {self.user} on"
            f"{self.reservation_date} for {self.number_of_guests} guests"
        )

    def clean(self):
        """Prevent saving or editing reservations
        in the past or overbooking."""
        super().clean()

        if self.reservation_date and self.time_slot:
            try:
                reservation_time = datetime.strptime(
                    self.time_slot, "%H:%M").time()
                reservation_datetime = datetime.combine(
                    self.reservation_date, reservation_time)
                reservation_datetime = timezone.make_aware(
                    reservation_datetime,
                    timezone.get_current_timezone()
                )

                if reservation_datetime < timezone.now():
                    raise ValidationError(
                        "Reservations cannot be set in the past.")
            except ValueError:
                raise ValidationError("Invalid time format for reservation.")

        # Prevent overbooking more than MAXIMUM_TABLES
            existing_count = Reservation.objects.filter(
                reservation_date=self.reservation_date,
                time_slot=self.time_slot
            ).exclude(id=self.id).count()

            if existing_count >= self.MAXIMUM_TABLES:
                raise ValidationError(
                    "Sorry, all tables are booked for this time slot.")

    def save(self, *args, **kwargs):
        """Ensure validation always runs when saving the model."""
        self.full_clean()
        super().save(*args, **kwargs)
