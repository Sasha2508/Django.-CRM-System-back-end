from django.contrib import admin
from .models import *


@admin.register(PhoneBook)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number'
    ]

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'address_1',
        'address_2',
        'city',
        'county',
        'postal_code',
        'country',
        'phone_book',
        'role'
    ]

