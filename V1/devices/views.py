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
        location_hash = json.loads(request.body)
        print(f'Here is the request information: {location_hash}')
        Location.objects.create(device=device,
                                lat=location_hash['location']['lat'],
                                long=location_hash['location']['long'])
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)
