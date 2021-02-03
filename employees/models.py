from django.db import models
from generalInfo.models import GeneralInfo
from django.contrib.auth.models import User
from clients.models import Client





class Department(models.Model):
    class Meta:
        db_table='departments'
        verbose_name='Department'
        verbose_name_plural='Departments'


    department_name = models.CharField(blank=False, null=False, max_length=20, verbose_name='Department Name')
    department_description = models.CharField(blank=False, null=False, max_length=60, verbose_name='Department Description')


    def __str__(self):
        return self.department_name


class Employee(models.Model):
    class Meta:
        db_table='employees'
        verbose_name= 'Employee'
        verbose_name_plural='Employees'

    user = models.ForeignKey(User, blank=False, null=False, verbose_name='Manager', on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=20, verbose_name='Occupation')
    hire_date = models.DateField(blank=False, null=False, max_length=8, verbose_name='Hiring Date')
    salary = models.FloatField(blank=False, null=False, max_length=10, verbose_name='Salary')
    #photo = models.ImageField(blank=False, null=False, verbose_name='Profile picture')
    department = models.ForeignKey(Department, blank=False, null=False, related_name='employees', verbose_name='Department', on_delete=models.CASCADE)
    general_info=models.ForeignKey(GeneralInfo, blank=False, null=False, verbose_name='General Info', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class EmployeeTodoListType(models.Model):
    class Meta:
        db_table= 'to_do_types'
        verbose_name= 'ToDo Type'
        verbose_name_plural='ToDo Types'

    title = models.CharField(blank=False, max_length=20, verbose_name='Title')

    def __str__(self):
        return self.title


class EmployeeToDoList(models.Model):
    class Meta:
        db_table='to_do_list'
        verbose_name='Task'
        verbose_name_plural='Tasks'

    type = models.ForeignKey(EmployeeTodoListType, blank=False, verbose_name='Type', on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=20, verbose_name='Title')
    description = models.TextField(blank=False, null=False, verbose_name='Description')
    user = models.ForeignKey(User, blank=False,null=False, related_name='to_do_list', verbose_name='Employee', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, blank=True, null=True, verbose_name='Client', on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True,blank=False, verbose_name='Time creation')
    time_action = models.DateTimeField(blank=True, verbose_name='Action time')

    def __str__(self):
        return self.title

