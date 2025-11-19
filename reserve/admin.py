from django.contrib import admin
from .models import Reservation

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'guest_name', 'guest_email', 'guest_phone',
        'reservation_date', 'time_slot', 'guestNo',
        'special_requests', 'seeAllergies')
    list_filter = ('reservation_date',)
    search_fields = ('user__username',)

    def guestNo(self, obj):
        return obj.number_of_guests
    guestNo.short_description = 'Guest No.'

    def seeAllergies(self, obj):
        return ", ".join([allergen.name for allergen in obj.allergies.all()])
    seeAllergies.short_description = 'Allergies'
