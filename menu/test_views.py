from menu.models import MenuItem
from menu.models import Allergen
from django.test import TestCase


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