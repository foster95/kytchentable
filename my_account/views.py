from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from cloudinary.models import CloudinaryField
from reserve.models import Reservation
from reserve.models import Reservation
from menu.models import Allergen
from datetime import date

# Create your views here.

"""
Show booking details
"""

@login_required
def my_account(request):
    reservations = (
        Reservation.objects
        .filter(user=request.user, reservation_date__gte=date.today())
        .order_by('reservation_date', 'time_slot')
    )
    context = {
        "reservations": reservations,
        "TIME_SLOTS": Reservation.TIME_SLOTS,
        "NO_GUESTS": Reservation.NO_GUESTS,
        "allergens": Allergen.objects.all(),
        "today": date.today().isoformat()
    }
    return render(request, "my_account/account.html", context)

"""
Allow guest to update booking
"""

@login_required
def update_reservation(request):
    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        booking = get_object_or_404(Reservation, id=booking_id, user=request.user)
        
        if not booking_id:
            messages.error(request, "No booking selected to update.")
            return redirect("my_account") 

        try:
            booking.guest_name = request.POST.get("guest_name")
            booking.guest_email = request.POST.get("guest_email")
            booking.guest_phone = request.POST.get("guest_phone")
            booking.reservation_date = request.POST.get("reservation_date")
            booking.time_slot = request.POST.get("time_slot")
            booking.number_of_guests = request.POST.get("number_of_guests")
            selected_allergens = request.POST.getlist("allergies")
            booking.special_requests = request.POST.get("special_requests")

            selected_allergies = request.POST.getlist("allergies")
            booking.allergies.set(selected_allergies)

            booking.full_clean()
            booking.save()

            messages.success(request, "Booking updated successfully.")
        except Exception as e:
            messages.error(request, f"Error updating booking: {e}")

    return redirect("my_reservations")

"""
Allow guest to delete reservation
"""

@login_required
def delete_reservation(request, booking_id):
    try:
        booking = get_object_or_404(Reservation, id=booking_id, user=request.user)
        booking.delete()
        messages.success(request, "Reservation deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting booking: {e}")

    return redirect("my_reservations")
