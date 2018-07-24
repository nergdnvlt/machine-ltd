from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.devices.models import Device
from V1.devices.serializers import DeviceSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json


class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)

    def update_location(self, request, device_id=None):
        print(f'Here is the request information: {request.data}')
        device = get_object_or_404(Device, id=device_id)
        device.update_location(request.data['location'])
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)
