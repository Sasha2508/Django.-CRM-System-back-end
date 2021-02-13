from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'general_info'
    ]

