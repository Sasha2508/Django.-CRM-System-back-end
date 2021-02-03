from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import ClientListSerializer, ClientSerializer
from rest_framework import permissions
import datetime
import json


class GetClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return Client.objects.filter(owner_id=self.request.user.id)

class CreateClient(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

