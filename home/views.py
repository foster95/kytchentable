from django.shortcuts import render
from django.http import HttpResponse 
from .models import HeroImage
from .models import ImageGallery

# Create your views here. 

"""
Display the home page.
"""

def home(request): 
    hero = HeroImage.objects.first()
    gallery = ImageGallery.objects.all()
    return render(
        request,
        'home/index.html',
        {
            'hero': hero,
            'gallery': gallery
        }
    )
