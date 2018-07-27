from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.devices.models import Device
from V1.locations.models import Location
from V1.devices.serializers import DeviceSerializer
from V1.locations.serializers import LocationSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from twilio.rest import Client
import os
import json

class TwilioService(self):
    twilio_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_token = os.environ['TWILIO_AUTH_TOKEN']
    self.client = Client(twilio_sid, twilio_token)

    def send_sms(self, number, lat, long):
        self.client.messages.create(
            to=number,
            from="+17205130638",
            body=f'You\'re asset has moved outside the geofence, it is at this location: lattitude: {lat}, and longitude {long}'
        )


# Phone number formatting - string - "+17196639883"
