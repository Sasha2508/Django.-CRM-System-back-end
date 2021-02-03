from django.db import models
from clients.models import Client
from employees.models import Employee
from django.contrib.auth.models import User
from cars.models import Car
# from cars.models import Car

#from products.models import ProductCatalog

class Order(models.Model):
    class Meta:
        db_table='orders'
        verbose_name='Order'
        verbose_name_plural='Orders'

    client = models.ForeignKey(Client, blank=False, null=False, max_length=20, related_name='orders', verbose_name='Client', on_delete=models.CASCADE)
    employee = models.ForeignKey(User, blank=False, null=False, max_length=20, related_name='orders', verbose_name='Employee', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, blank=False, null=False, verbose_name='Car', on_delete=models.CASCADE)
    description = models.CharField(blank=False, null=False, max_length=40, verbose_name='Description')
    date_creation = models.DateTimeField(blank=False, null=False, max_length=14, verbose_name='Order Date/Time')
    date_completion = models.DateTimeField(blank=False, null=False, max_length=13, verbose_name='Completion Date/Time')
    sales_tax = models.FloatField(blank=False, null=False, max_length=10, verbose_name='Sales Tax')
    discount = models.FloatField(blank=False, null=False, max_length=10, verbose_name='Discount')
    trade_in = models.FloatField(blank=True, null=True, max_length=10, verbose_name='Trade In')
    total_price = models.FloatField(blank=False, null=False, max_length=10, verbose_name='Total Price')
    payment = models.CharField(blank=False, null=False, max_length=20, verbose_name='Payment method')
    transaction_status = models.CharField(blank=False, null=False, max_length=20, verbose_name='Transaction Status')

    #catalog = models.ForeignKey(ProductCatalog, blank=False, null=False, related_name='orders', verbose_name='Catalog', on_delete=models.CASCADE)

    def __str__(self):
        return self.description