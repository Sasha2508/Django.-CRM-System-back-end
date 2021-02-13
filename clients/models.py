from django.db import models
from django.contrib.auth import get_user_model
from generalInfo.models import GeneralInfo

User = get_user_model()

class Client(models.Model):
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    owner = models.ForeignKey(User, blank=False, null=False, verbose_name='Manager', on_delete=models.CASCADE)
    #first_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='First name')
    #last_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='Last name')
    description = models.TextField(blank=False, null=False, verbose_name='Description')
    general_info = models.ForeignKey(GeneralInfo, blank=False, null=False, related_name='clients', verbose_name='General Info', on_delete=models.CASCADE)


    def __str__(self):
        return self.general_info.first_name + " " + self.general_info.last_name

    def __unicode__(self):
        return self.general_info.first_name + " " + self.general_info.last_name

