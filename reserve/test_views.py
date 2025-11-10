from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from menu.models import Allergen
from reserve.models import Reservation
from reserve.forms import ReservationForm


class TestReservationViews(TestCase):
    """Basic tests for the reservation form and submission"""

    def setUp(self):
        """Set up test user and allergen"""
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            email="test@example.com"
        )
        self.allergen = Allergen.objects.create(name="Nuts")
        self.client.login(username="testuser", password="password123")

    def test_reservation_form_renders(self):
        """Test the reservation form page loads correctly"""
        response = self.client.get(reverse("reserve"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["form"], ReservationForm,
            msg="Reservation form did not render correctly."
        )

    def test_successful_reservation_submission(self):
        """Test a valid form submission creates a reservation"""
        self.client.post(reverse("reserve"), {
            "guest_name": "Test Name",
            "guest_email": "test@example.com",
            "guest_phone": "0987654321",
            "reservation_date": date.today().strftime("%Y-%m-%d"),
            "time_slot": "18:00",
            "number_of_guests": 2,
            "allergies": [self.allergen.id],
            "special_requests": "Window seat"
        }, follow=True)

        self.assertTrue(
            Reservation.objects.filter(guest_name="Test Name").exists(),
            msg="Reservation was not successfully created."
        )
