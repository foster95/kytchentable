from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('Entree', 'Entree'),
    ('Main', 'Main Course'),
    ('Side', 'Side Dish'),
    ('Dessert', 'Dessert'),
]

class Allergen(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class MenuItem(models.Model):

    """
    Stores information about a menu item.
    """

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    description = models.TextField()
    allergen = models.ManyToManyField(Allergen, blank=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
