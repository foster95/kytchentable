from menu.models import MenuItem
from menu.models import Allergen
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestMenuItemModel(TestCase):

    def test_menu_renders_name(self):
        """Test that MenuItem string representation returns the item name"""
        item = MenuItem.objects.create(
            category='Dessert',
            name='Dark Cherry & Coconut Pavlova',
            description='A crisp, chewy meringue made from aquafaba.',
        )
        item.allergen.set([])

        self.assertEqual(str(item), 'Dark Cherry & Coconut Pavlova')

    def test_menu_item_requires_name(self):
        """MenuItem should raise ValidationError if 'name' is missing"""
        item = MenuItem(
            category='Dessert',
            description='A crisp, chewy meringue made from aquafaba.',
        )

        with self.assertRaises(ValidationError):
            item.full_clean()

    def test_menu_item_allergens_relationship(self):
        """Test that MenuItem can have multiple allergens associated"""
        item = MenuItem.objects.create(
            category='Dessert',
            name='Dark Cherry & Coconut Pavlova',
            description='A crisp, chewy meringue made from aquafaba.',
        )
        allergen1 = Allergen.objects.create(name='Nuts')
        allergen2 = Allergen.objects.create(name='Dairy')

        item.allergen.set([allergen1, allergen2])

        self.assertIn(allergen1, item.allergen.all())
        self.assertIn(allergen2, item.allergen.all())
