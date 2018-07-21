from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from api.models import User, Device
from api.serializers import UserSerializer, DeviceSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json


class UserViews(viewsets.ViewSet):

    def create(self, request):
        user_attrs = request.data['user']
        if 'username' in user_attrs.keys() and 'phone_number' in user_attrs.keys() and 'device_number' in user_attrs.keys():
            user = User.objects.create(name=food_attrs['name'], calories=food_attrs['calories'])
            serializer = UserSerializer(food)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        print(request.data)

    def update(self, request, pk=None):
        print(request.data)

    def delete(self, request, pk=None):
        print(request.data)


class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)

    def update_location(self, request, device_id=None):
        print(request.data)
