from rest_framework import serializers
from .models import *


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'user',
            'title',
            #'hire_date',
            'salary',
            #'department',
            #'general_info'
        ]

    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class ToDoTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTodoListType
        fields = [
            'title'
        ]

    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class ToDoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTodoListType
        fields = '__all__'

    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())



class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeToDoList
        fields = '__all__'

    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeToDoList
        fields= '__all__'

    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'department_name'
        ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields ="__all__"



