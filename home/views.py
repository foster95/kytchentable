from django.shortcuts import render
from django.http import HttpResponse 
from .models import HeroImage

# Create your views here. 

"""
Display the home page.
"""

def home(request): 
    hero = HeroImage.objects.first()
    return render(
        request,
        'home/index.html',
        {
            'hero': hero
        }
    )
