from django.contrib import admin
from .models import MenuItem
from .models import Allergen

# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'tasting_order')
    list_editable = ('tasting_order',)
    list_filter = ('category',)
    ordering = ('category', 'tasting_order', 'name')


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
