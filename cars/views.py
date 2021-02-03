from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend



class GetBrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filter_fields = [
        'title',
        'country'
    ]


class GetCarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filter_fields = [
        'brand',
        'title',
        'generation'
    ]
    search_fields = [
        'title'
    ]
    ordering_fields = [
        'brand',
        'title'
    ]