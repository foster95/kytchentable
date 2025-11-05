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

@login_required
def reservation(request):
    reserve = Reservation.objects.all()
    reservation_form = ReservationForm()

    if request.method == 'POST':

        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to make a reservation.')
            return redirect('login')

        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  
            reservation.save()

            messages.success(request, 'Your reservation has been submitted successfully!')
            return redirect('reserve')
        else:
            messages.error(request, 'There was an error with your reservation. Please try again.')
            return redirect('reserve')
    else:
        form = ReservationForm()

    return render(request, 'reserve/reserve.html', {
        'form': form,
        'reservations': reserve
    })