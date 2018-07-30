from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.locations.services import LocationService
from V1.devices.models import Device
from V1.locations.models import Location
from V1.locations.serializers import LocationSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class LocationViews(viewsets.ViewSet):

    def create(self, request, device_id=None):
        added_location = LocationService().create_location(request, device_id)
        return added_location

    def index(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        locations = device.locations.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
