from django.contrib import admin
from django import forms
from .models import MenuItem
from .models import Allergen

# Register your models here.


class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
        widgets = {
            'allergens': forms.CheckboxSelectMultiple(),
        }


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemAdminForm
    list_display = ('name', 'category', 'tasting_order')
    list_editable = ('tasting_order',)
    list_filter = ('category',)
    ordering = ('category', 'tasting_order', 'name')


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
