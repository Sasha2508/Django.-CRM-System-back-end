from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
import json
import datetime


class GetEmployeeList(generics.ListAPIView):
    #queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return Employee.objects.filter(user_id=self.request.user.id)


class CreateEmployee(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class GetToDoTypeList(generics.ListAPIView):
    #queryset = EmployeeTodoListType.objects.all()
    serializer_class = ToDoTypeListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return EmployeeTodoListType.objects.filter(user_id=self.request.user.id)


class CreateToDoType(generics.CreateAPIView):
    serializer_class = ToDoTypeSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class GetToDoList(generics.ListAPIView):
    queryset = EmployeeToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = [
         permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return EmployeeToDoList.objects.filter(user_id=self.request.user.id)

class CreateToDo(generics.CreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

class GetDepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filter_fields = [
        'department_name'
    ]

class CreateDepartment(generics.CreateAPIView):
    serializer_class = DepartmentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filter_fields = [
        'department_name'
    ]
    search_fields = [
        'department_name'
    ]
    ordering_fields = [
        'department_description'
    ]


