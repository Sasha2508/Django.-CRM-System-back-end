from django.db import models

class Brand(models.Model):
    class Meta:
        db_table = 'brands'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    title = models.CharField(blank=False, null=False, max_length=50, verbose_name='Brand Name')
    country = models.CharField(blank=False, null=False, max_length=50, verbose_name='Country')


    def __str__(self):
        return self.title


class Car(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    title = models.CharField(blank=False, null=False, max_length=50, verbose_name='Car Model')
    brand = models.ForeignKey(Brand, blank=False, null=False, related_name= 'cars', verbose_name='Brand', on_delete=models.CASCADE)
    generation = models.CharField(blank=True, null=True, max_length=30, verbose_name='Generation')

    def __str__(self):
        return self.brand.title + " " + self.title + " " + self.generation

TRANSMISSIONS = (
    ('A', 'Automate'),
    ('M', 'Manual'),
    ('R', 'Robot'),
    ('V', 'Variator')
)

STATUS = (
    ('A', 'Available'),
    ('S', 'Sold'),
    ('R', 'Reserved'),
    ('O', 'Ordered')
)

CYLINDERS = (
    ('A', '4'),
    ('B', '5'),
    ('C', '6'),
    ('D', '8'),
    ('E', '12')
)


class CarItem(models.Model):
    class Meta:
        db_table = 'cars_items'
        verbose_name = 'Car Item'
        verbose_name_plural = 'Cars Items'

    car = models.ForeignKey(Car, related_name='car_items', blank=False, null=False, verbose_name='Car', on_delete=models.CASCADE)
    production_date = models.DateField(blank=False, null=False, verbose_name= 'Date of Production')
    color = models.CharField(blank=False, null=False, max_length=20, verbose_name='Color')
    model_year = models.CharField(blank=False, null=False, max_length=4, verbose_name='Model year')
    transmission = models.CharField(default='A', choices= TRANSMISSIONS, max_length=1, blank=False, null=False, verbose_name='Transmission')
    vin = models.CharField(blank=False, null=False, max_length=30, verbose_name='VIN')
    status = models.CharField(default='A', choices=STATUS, max_length=1, blank=False, null=False, verbose_name='Status')
    cylinders = models.CharField(default='A', choices=CYLINDERS, max_length=1, blank=False, null=False, verbose_name='Cylinders')
    price = models.CharField(blank=False, max_length=8, null=False, verbose_name='Price')
    trim = models.CharField(blank=False, max_length=20, null=False, verbose_name='Trim')
    engine_volume = models.CharField(blank=False, max_length= 20, null= False, verbose_name='Engine Volume')

    def __str__(self):
        return self.vin + " - " + self.car.brand.title + " " + self.car.title



