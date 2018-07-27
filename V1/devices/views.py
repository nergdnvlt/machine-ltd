from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.devices.models import Device
from V1.locations.models import Location
from V1.devices.serializers import DeviceSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json

from IPython import embed

class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)

    def update_location(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        location = request.data['location']
        print(f'Here is the request information: {location}')
        Location.objects.create(device=device,
                                lat=location[0],
                                long=location[1])
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)
