from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'department_name',
        'department_description'
    ]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'hire_date',
        'department',
        'general_info'
    ]

@admin.register(EmployeeTodoListType)
class EmployeeTodoListType(admin.ModelAdmin):
    list_display = [
        'title'
    ]

@admin.register(EmployeeToDoList)
class EmployeeToDoListAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'type',
        'user',
        'client',
        'time_creation',
        'time_action'
    ]
