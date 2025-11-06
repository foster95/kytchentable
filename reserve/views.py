from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation

@login_required
def reservation(request):
    reserve = Reservation.objects.all()

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  
            reservation.save()
            form.save_m2m()
            messages.success(request, 'Your reservation has been submitted successfully!')
            return redirect('reserve')
        else:
            
            return render(request, 'reserve/reserve.html', {
                'form': form,
                'reservations': reserve
            })
    else:
        form = ReservationForm()

    return render(request, 'reserve/reserve.html', {
        'form': form,
        'reservations': reserve
    })
