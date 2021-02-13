from django.contrib import admin
from .models import *
from django.utils import html


@admin.register(PhoneBook)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number',
        'general_info'
    ]
    list_filter = [
        'general_info'
    ]

class PhonesInLine(admin.StackedInline):
    model = PhoneBook
    extra = 0


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
        'role',
        'get_primary_phone'
    ]
    inlines = [
        PhonesInLine
    ]


    def get_primary_phone(self, obj):
        try:
            phones = PhoneBook.objects.filter(general_info=obj)
            return html.format_html('<a href="/admin/generalInfo/phonebook/?general_info__id__exact='+str(obj.id)+'">'+phones.first().phone_number+' ('+str(len(phones))+')</a>')
        except BaseException:
            return "-"
    get_primary_phone.short_description = 'Phones'







