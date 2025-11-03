from django.contrib import admin
from .models import MenuItem
from .models import Allergen

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  
    list_filter = ('category',)  
    search_fields = ('name', 'description')  
    filter_horizontal = ('allergen',)  


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
