from django.urls import path
from . import views
from .views import my_account

urlpatterns = [
    path('', my_account, name='my_reservations'),
    path('update_reservation/', views.update_reservation, name="update_reservation")

]
