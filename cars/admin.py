from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'country'
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'brand',
        'generation'
    ]

@admin.register(CarItem)
class CarItemAdmin(admin.ModelAdmin):
    list_display = [
        'vin',
        'car',
        'production_date',
        'color',
        'transmission',
        'status',
        'price'
    ]

