from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here. 

"""
Display the home page.
"""

def home(request): 
    return render(
        request,
        'home/index.html', 
    )
