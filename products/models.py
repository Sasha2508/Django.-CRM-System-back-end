# from django.db import models
# from employees.models import *
#
# class ProductCatalog(models.Model):
#     class Meta:
#         db_table = 'products_catalog'
#         verbose_name = 'Product Catalog'
#         verbose_name_plural = 'Products Catalog'
#
#     name_of_service = models.CharField(blank=False, null=False, max_length=40, verbose_name='Name of service')
#     # employee = models.ForeignKey(Employee, )
#
#     def __str__(self):
#         return self.name_of_service
#
# class Service(models.Model):
#     class Meta:
#         db_table = 'services'
#         verbose_name = 'Service'
#         verbose_name_plural = 'Services'
#
#     title = models.CharField(blank=False, null=False, max_length=20, verbose_name='Title')
#     description = models.CharField(blank=False, null=False, max_length=40, verbose_name='Description')
#     price = models.FloatField(blank=False, null=False, max_length=6, verbose_name='Price of service')
#     catalog = models.ForeignKey(ProductCatalog, blank=False, null=False, related_name='services', verbose_name='Catalog', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
# class Accessory(models.Model):
#     class Meta:
#         db_table = 'accessories'
#         verbose_name = 'Accessory'
#         verbose_name_plural = 'Accessories'
#
#
#     title = models.CharField(blank=False, null=False, max_length=20, verbose_name='Title')
#     description = models.CharField(blank=False, null=False, max_length=40, verbose_name='Description')
#     price = models.FloatField(blank=False, null=False, max_length=6, verbose_name='Price of accessory')
#     catalog = models.ForeignKey(ProductCatalog, blank=False, null=False, related_name='accessories', verbose_name='Catalog', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
