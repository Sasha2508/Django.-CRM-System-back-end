from rest_framework import serializers
from .models import *

class CarItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = [
            'id',
            'vin',
            'car',
            'production_date',
            'color',
            'transmission',
            'status'
        ]

class CarListSerializer(serializers.ModelSerializer):
    car_items = CarItemListSerializer(many=True)
    class Meta:
        model = Car
        fields = [
            'id',
            'title',
            'brand',
            'generation',
            'car_items'
        ]


class BrandListSerializer(serializers.ModelSerializer):
    cars = CarListSerializer(many=True)
    class Meta:
        model = Brand
        fields = [
            'id',
            'title',
            'country',
            'cars'
        ]



