from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from menu.models import Allergen

# Create your models here.

OPENING_HOURS = {
        'Tuesday': ('11:00 AM', '10:00 PM'),
        'Wednesday': ('11:00 AM', '10:00 PM'),
        'Thursday': ('11:00 AM', '10:00 PM'),
        'Friday': ('10:00 AM', '11:00 AM'),
        'Saturday': ('10:00 AM', '11:00 AM'),
        'Sunday': ('10:00 AM', '8:00 PM'),
        'Monday' : None,
    }

"""

Model to store reservation details.

"""

class Reservation(models.Model):

    NO_GUESTS = [(i, str(i)) for i in range(1, 7)]  # Options for number of guests from 1 to 7

    TIME_SLOTS = [
        ('10:00 AM', '10:00 AM'),
        ('10:15 AM', '10:15 AM'),
        ('10:30 AM', '10:30 AM'),
        ('10:45 AM', '10:45 AM'),
        ('11:00 AM', '11:00 AM'),
        ('11:15 AM', '11:15 AM'),
        ('11:30 AM', '11:30 AM'),
        ('11:45 AM', '11:45 AM'),
        ('12:00 PM', '12:00 PM'),
        ('12:15 PM', '12:15 PM'),
        ('12:30 PM', '12:30 PM'),
        ('12:45 PM', '12:45 PM'),
        ('1:00 PM', '1:00 PM'),
        ('1:15 PM', '1:15 PM'),
        ('1:30 PM', '1:30 PM'),
        ('1:45 PM', '1:45 PM'),
        ('2:00 PM', '2:00 PM'),
        ('2:15 PM', '2:15 PM'),
        ('2:30 PM', '2:30 PM'), 
        ('2:45 PM', '2:45 PM'),
        ('3:00 PM', '3:00 PM'),
        ('3:15 PM', '3:15 PM'),
        ('3:30 PM', '3:30 PM'),
        ('3:45 PM', '3:45 PM'),
        ('4:00 PM', '4:00 PM'),
        ('4:15 PM', '4:15 PM'),
        ('4:30 PM', '4:30 PM'),
        ('4:45 PM', '4:45 PM'),
        ('5:00 PM', '5:00 PM'),
        ('5:15 PM', '5:15 PM'),
        ('5:30 PM', '5:30 PM'),
        ('5:45 PM', '5:45 PM'),
        ('6:00 PM', '6:00 PM'),
        ('6:15 PM', '6:15 PM'),
        ('6:30 PM', '6:30 PM'),
        ('6:45 PM', '6:45 PM'),
        ('7:00 PM', '7:00 PM'),
        ('7:15 PM', '7:15 PM'),
        ('7:30 PM', '7:30 PM'),
        ('7:45 PM', '7:45 PM'),
        ('8:00 PM', '8:00 PM'),
        ('8:15 PM', '8:15 PM'),
        ('8:30 PM', '8:30 PM'),
        ('8:45 PM', '8:45 PM'),
        ('9:00 PM', '9:00 PM'),
        ('9:15 PM', '9:15 PM'),
        ('9:30 PM', '9:30 PM'),
        ('9:45 PM', '9:45 PM'),
        ('10:00 PM', '10:00 PM'),
        ('10:15 PM', '10:15 PM'),
        ('10:30 PM', '10:30 PM'),
        ('10:45 PM', '10:45 PM'),
        ('11:00 PM', '11:00 PM'),
    
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

