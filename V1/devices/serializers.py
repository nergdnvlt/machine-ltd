from rest_framework import serializers
from V1.locations.serializers import LocationSerializer
from V1.devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = [
            'id',
            'sms_number',
            'pin_lat',
            'pin_long',
            'radius',
            'locations',
        ]
