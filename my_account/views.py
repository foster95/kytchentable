from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from reserve.models import Reservation

# Create your views here.

@login_required
def my_account(request):
    reservations = Reservation.objects.filter(
        user=request.user,
        reservation_date__gte=timezone.now()
    ).order_by('reservation_date')

    return render(request, 'my_account/account.html', {
        'reservations': reservations,
    })