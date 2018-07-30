import json
from service_objects.services import Service
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from V1.locations.models import Location
from V1.devices.models import Device
from V1.locations.serializers import LocationSerializer
from V1.devices.serializers import DeviceSerializer
from V1.devices.services import TwilioService
from rest_framework import status

class LocationService(Service):

    def create_location(self, request, device_id):
        data = json.loads(request.body)
        device = get_object_or_404(Device, id=device_id)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            location = serializer.save(device=device)
            if location:
                serializer = DeviceSerializer(device, many=False)
                if device.radius <= location.distance:
                    message = TwilioService().send_sms(device.user.phone_number, location.lat, location.long)
                    return Response({"device": serializer.data, "message": message}, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
