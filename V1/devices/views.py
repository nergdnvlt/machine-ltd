from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.devices.models import Device
from V1.users.models import User
from V1.devices.serializers import DeviceSerializer
from V1.devices.services import DeviceService
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class DeviceViews(viewsets.ViewSet):

    def list(self, request, username=None):
        user = get_object_or_404(User, username=username)
        devices = user.devices.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, username=None):
        create_response = DeviceService().create_device(request, username)
        return create_response

    def update(self, request, device_id=None):
        device_info = DeviceService().update_device(request, device_id)
        return device_info

    def partial_update(self, request, device_id=None):
        device_info = DeviceService().update_device(request, device_id)
        return device_info

    def destroy(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        device.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
