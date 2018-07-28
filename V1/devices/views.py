from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.devices.models import Device
from V1.locations.models import Location
from V1.devices.serializers import DeviceSerializer
from V1.locations.serializers import LocationSerializer
from V1.devices.services import TwilioService
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json

class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def add_location(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        location = self.__parse_location_data__(device, request)
        if location.id:
            serializer = DeviceSerializer(device, many=False)
            if device.radius <= location.distance:
                message = TwilioService().send_sms(device.user.phone_number, location.lat, location.long)
                return Response({"device": serializer.data, "message": message}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_303_SEE_OTHER)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def __parse_location_data__(self, device, request):
        location = json.loads(request.body)
        loc_lat = float(location['lat'])
        loc_long = float(location['long'])
        location = Location(device=device, lat=loc_lat, long=loc_long)
        location.save()
        return location
