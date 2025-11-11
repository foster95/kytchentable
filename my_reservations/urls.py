from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_reservations, name='my_reservations'),
    path(
        'update_reservation/',
        views.update_reservation,
        name="update_reservation"
        ),
    path(
        'delete_reservation/<int:booking_id>/',
        views.delete_reservation,
        name="delete_reservation"
        ),
]
