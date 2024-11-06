from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):  # or use admin.StackedInline
    model = CarModel
    extra = 1


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'year', 'car')
    search_fields = ('model_name', 'car__name')
    list_filter = ('year', 'car')
    ordering = ('-year',)


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)


# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
