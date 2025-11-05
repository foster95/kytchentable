from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from cloudinary.models import CloudinaryField
from reserve.models import Reservation
from reserve.models import Reservation

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from reserve.models import Reservation

@login_required
def my_account(request):
    reservations = Reservation.objects.filter(user=request.user)  # ✅ always define
    context = {
        "reservations": reservations,
        "TIME_SLOTS": Reservation.TIME_SLOTS,
        "NO_GUESTS": Reservation.NO_GUESTS,
    }
    return render(request, "my_account/account.html", context)

@login_required
def update_reservation(request):
    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        booking = get_object_or_404(Reservation, id=booking_id, user=request.user)
        
        if not booking_id:
            messages.error(request, "No booking selected to update.")
            return redirect("my_account") 

        try:
            booking.reservation_date = request.POST.get("reservation_date")
            booking.time_slot = request.POST.get("time_slot")
            booking.number_of_guests = request.POST.get("number_of_guests")
            booking.special_requests = request.POST.get("special_requests")
            booking.save()
            messages.success(request, "Booking updated successfully.")
        except Exception as e:
            messages.error(request, f"Error updating booking: {e}")

    return redirect("my_account")

