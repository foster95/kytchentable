from django import path
from .views import my_account

urlpatterns = [
    path('', my_account, name='my_account'),

]
