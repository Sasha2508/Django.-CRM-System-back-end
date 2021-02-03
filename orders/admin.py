from django.contrib import admin
from .models import *



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'date_creation',
        'date_completion',
        'sales_tax',
        'discount',
        'trade_in',
        'total_price',
        'payment',
        'transaction_status',
        #'catalog'
    ]

    list_filter = [
        'client',
        'employee',
        'date_creation'
    ]

    # search_fields = [
    #     'client__first_name',
    #     'client__last_name',
    #     'employee__first_name',
    #     'employee__last_name',
    #     'date_creation'
    # ]