from rest_framework import serializers
from .models import *


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'owner',
            'description'
        ]

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())