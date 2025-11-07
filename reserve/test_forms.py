from django.test import TestCase
from django.contrib.auth.models import User
from reserve.forms import ReservationForm
from menu.models import Allergen
from reserve.models import Reservation
from datetime import date


class TestReservationForm(TestCase):
    """Tests for ReservationForm"""

    def setUp(self):
        """Create test user and allergen"""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.allergen = Allergen.objects.create(name="Test Allergen")

    def test_form_is_valid(self):
        """Tests if reservation form is valid"""
        reservation_form = ReservationForm({
            'guest_name': 'Test',
            'guest_email': 'test@example.com',
            'guest_phone': '1234567890',
            'reservation_date': date.today().strftime("%Y-%m-%d"),
            'time_slot': '18:00',
            'number_of_guests': 2,
            'allergies': [self.allergen.id],
            'special_requests': 'Window seat please'
        })
        self.assertTrue(reservation_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """Tests if reservation form is invalid"""
        reservation_form = ReservationForm({
            'guest_name': '',  # Missing required name
            'guest_email': 'not-an-email',
            'guest_phone': '',
            'reservation_date': '',
            'time_slot': '',
            'number_of_guests': '',
            'allergies': [self.allergen.id],
            'special_requests': ''
        })
        self.assertFalse(reservation_form.is_valid(), msg='Form is valid')

    def test_form_is_invalid_due_to_overbooking(self):
        """ Tests if overbooking raises a validation error"""
        
        # Fill up all available tables
        for _ in range(Reservation.MAXIMUM_TABLES):
            Reservation.objects.create(
                user=self.user,
                guest_name="Test User",
                guest_email="test@example.com",
                guest_phone="1234567890",
                reservation_date=date.today(),
                time_slot="19:00",
                number_of_guests=2,
            )

        # Attempt to create one more reservation in the same slot
        reservation_form = ReservationForm({
            'guest_name': 'Extra Guest',
            'guest_email': 'extra@example.com',
            'guest_phone': '0987654321',
            'reservation_date': date.today().strftime("%Y-%m-%d"),
            'time_slot': '19:00',
            'number_of_guests': 2,
            'allergies': [self.allergen.id],
            'special_requests': ''
        })

        # Expect form to be invalid (overbooking triggered)
        self.assertFalse(reservation_form.is_valid(), msg='Form should be invalid due to overbooking.')

        # Check that the correct message appears
        self.assertIn(
            'Sorry, all tables are booked for this time slot.',
            str(reservation_form.errors),
            msg='Overbooking error message not found in form errors.'
        )

