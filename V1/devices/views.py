from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.devices.models import Device
from V1.locations.models import Location
from V1.devices.serializers import DeviceSerializer
from V1.locations.serializers import LocationSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json

class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.save()
            if device.id:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, device_id=None):
        device_info = self.__device_update__(request, device_id)
        return device_info

    def partial_update(self, request, device_id=None):
        device_info = self.__device_update__(request, device_id)
        return device_info

    def __device_update__(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.update(instance=device, validated_data=serializer.data)
            if device:
                res_serializer = DeviceSerializer(device, many=False)
                return Response(res_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
