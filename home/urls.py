from djangos.url import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]