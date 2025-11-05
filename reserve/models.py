from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from menu.models import Allergen

# Create your models here.

"""
Model to store reservation details.

"""
class Reservation(models.Model):

    NO_GUESTS = [(i, str(i)) for i in range(1, 7)]  # Options for number of guests from 1 to 7

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)
    number_of_guests = models.PositiveIntegerField(choices=NO_GUESTS)
    allergies = models.ManyToManyField(Allergen, blank=True)
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-reservation_date', 'time_slot']

    def __str__(self):
        return f"Reservation for {self.user} on {self.reservation_date} for {self.number_of_guests} guests"

