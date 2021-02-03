from django.db import models
#from clients.models import Client
#from django.contrib.auth.models import User


class PhoneBook(models.Model):
    class Meta:
        db_table='phones_book'
        verbose_name='Phone Book'
        verbose_name_plural='Phones Book'

    phone_number = models.CharField(blank=False, null=False, max_length=20, verbose_name='Phone number')

    def __str__(self):
        return self.phone_number


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('-', 'Not mentioned')
)

STATE = (
    ('-', 'Not mentioned'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
)

class GeneralInfo(models.Model):
    class Meta:
        db_table='general_info'
        verbose_name='Info Log'
        verbose_name_plural='Info Logs'

    first_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='First Name')
    middle_name = models.CharField(blank=True, null=True, max_length=20, verbose_name='Middle Name/ Patronymic Name')
    last_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='Last Name')
    date_of_birth = models.DateField(blank=False, null=False, max_length=8, verbose_name='Date of Birth')
    gender = models.CharField( default='-', choices=GENDER, blank=False, null=False, max_length=1, verbose_name='Gender')
    address_1 = models.CharField(blank=True, null=True, max_length=40, verbose_name='Address 1')
    address_2 = models.CharField(blank=False, null=False, max_length=30, verbose_name='Address 2')
    city = models.CharField(blank=False, null=False, max_length=20, verbose_name='City')
    county = models.CharField(blank=False, null=False, max_length=20, verbose_name='County')
    state = models.CharField(default='-', choices=STATE, blank=False, null=False, max_length=2, verbose_name='State')
    postal_code = models.CharField(blank=False, null=False, max_length=14, verbose_name='Postal Code')
    country = models.CharField(blank=False, null=False, max_length=20, verbose_name='Country')
    phone_book = models.ForeignKey(PhoneBook, blank=False, null=False, related_name='general_info', verbose_name='Phone Book', on_delete=models.CASCADE)
    role = models.CharField(blank=False, null=False, max_length=10, verbose_name='Client or Employee')

    def __str__(self):
        return self.first_name + " " + self.last_name









