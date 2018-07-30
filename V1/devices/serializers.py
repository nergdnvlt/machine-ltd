from rest_framework import serializers
from V1.locations.serializers import LocationSerializer
from V1.devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    sms_number = serializers.CharField(max_length=100)
    pin_lat = serializers.FloatField()
    pin_long = serializers.FloatField()
    radius = serializers.FloatField(default=500)
    alert = serializers.BooleanField(default=True)
    last_location = LocationSerializer(many=False, read_only=True, source='latest_location')

    class Meta:
        model = Device
        fields = [
            'id',
            'sms_number',
            'pin_lat',
            'pin_long',
            'radius',
            'alert',
            'last_location',
        ]
        extra_kwargs = {
            'user': {'required': False},
            'id': {'required': False},
            'radius': {'required': False},
            'alert': {'required': False},
            'last_location': {'required': False}
        }
