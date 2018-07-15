from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from api.models import Device
from api.serializers import DeviceSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json

from IPython import embed
# Create your views here.


class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)

    def update(self, request, device_id=None):
        embed()
