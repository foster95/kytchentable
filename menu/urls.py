from django.urls import path
from .views import philosophy

urlpatterns = [
    path('', philosophy, name='philosophy'),
]