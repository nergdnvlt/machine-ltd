from twilio.rest import Client
from V1.devices.models import Device
from V1.users.models import User
from django.shortcuts import get_object_or_404
from service_objects.services import Service
from V1.devices.serializers import DeviceSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class TwilioService(Service):

    def __init__(self):
        self.twilio_sid = settings.TWILIO_SID
        self.twilio_token = settings.TWILIO_AUTH
        self.client = Client(self.twilio_sid, self.twilio_token)

    def send_sms(self, number, lat, long):
        url = f'http://maps.google.com/?q={lat},{long}'
        message = self.client.messages.create(
            to=number,
            from_='+17205130638',
            body=f'Moving asset. Location: latitude: {lat}, and longitude {long}. {url}'
        )
        return message.body

class DeviceService(Service):

    def create_device(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.save(user=user)
            if device.id:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_device(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.update(instance=device, validated_data=serializer.data)
            if device:
                res_serializer = DeviceSerializer(device, many=False)
                return Response(res_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
