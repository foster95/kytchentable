from reserve.forms import ReservationForm
from menu.models import Allergen
from reserve.models import Reservation
from datetime import date, timedelta
from django.test import TestCase
from django.contrib.auth.models import User


class TestMyReservationsPage(TestCase):
    """ Tests for my reservations page """
    def setUp(self):
        """ Create test user and reservations """
        self.user = User.objects.create_user(
            username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

    def test_my_account_page_shows_upcoming_reservations(self):
        """ Test that only upcoming reservations are shown
        from my account page """
        upcoming_reservation = Reservation.objects.create(
            user=self.user,
            guest_name="Test User",
            guest_email="test@test.com",
            guest_phone="0987654321",
            reservation_date=date.today() + timedelta(days=1),
            time_slot="19:00",
            number_of_guests=4,
        )