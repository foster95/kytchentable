from django.shortcuts import render

# Create your views here.

"""
Display philosophy page.
"""


def philosophy(request):
    return render(
        request,
        'philosophy/philosophy.html',
    )
