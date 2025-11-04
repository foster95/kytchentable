from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation

# Create your views here.


"""

Creates reservation form to allow authenticated
users to make reservations.

"""

def reservation(request):
    reserve = Reservation.objects.all()
    reservation_form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  
            reservation.save()

            messages.success(request, 'Your reservation has been submitted successfully!')
            return redirect('reserve')
        else:
            messages.error(request, 'There was an error with your reservation. Please try again.')
    else:
        form = ReservationForm()

    return render(request, 'reserve/reserve.html', {
        'form': form,
        'reservations': reserve
    })