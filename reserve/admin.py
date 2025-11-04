from django.contrib import admin
from .models import Reservation

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reservation_date', 'time_slot', 'number_of_guests', 'special_requests')
    list_filter = ('reservation_date',)
    search_fields = ('user__username',)

