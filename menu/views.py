from django.shortcuts import render
from .models import MenuItem

# Create your views here.


def menu(request):
    menu_items = {
        'entrees': MenuItem.objects.filter(category='Entree'),
        'mains': MenuItem.objects.filter(category='Main'),
        'side': MenuItem.objects.filter(category='Side'),
        'desserts': MenuItem.objects.filter(category='Dessert'),
        'tasting': (
            MenuItem.objects    
            .filter(category='Tasting')
            .order_by('tasting_order'),
        ),
    }
    return render(
        request, 'menu/menu.html',
        {'menu_items': menu_items})


def tasting_menu(request):
    items = MenuItem.objects.filter(category='Tasting'
                                    ).order_by('tasting_order')
    return render(request, 'menu/tasting_menu.html', {'items': items})


def a_la_carte_menu(request):
    items = MenuItem.objects.exclude(category='Tasting'
                                     ).order_by('category', 'name')
    return render(request, 'menu/a_la_carte.html', {'items': items})
