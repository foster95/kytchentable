from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def menu(request):
    menu_items = {
        'entrees': MenuItem.objects.filter(category='Entree'),
        'mains': MenuItem.objects.filter(category='Main'),
        'side': MenuItem.objects.filter(category='Side'),
        'desserts': MenuItem.objects.filter(category='Dessert'),
        'tasting': MenuItem.objects.filter(category='Tasting'),
    }
    return render(
        request, 'menu/menu.html', 
        {'menu_items': menu_items})