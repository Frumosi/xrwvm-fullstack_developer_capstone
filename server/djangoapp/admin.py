from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class


class CarModelInline(admin.TabularInline):  # or use admin.StackedInline
    model = CarModel
    extra = 1

# CarModelAdmin class


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'year', 'car')  # Fields to display in the list view
    search_fields = ('model_name', 'car__name')   # Fields to enable search functionality
    list_filter = ('year', 'car')                 # Fields to filter by in the sidebar
    ordering = ('-year',)                         # Ordering of the list (e.g., descending by year)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')       # Fields displayed in the CarMake list view
    search_fields = ('name', 'description')      # Search functionality for CarMake
    list_filter = ('name',)                      # Filter CarMakes by country

# Register models here

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
