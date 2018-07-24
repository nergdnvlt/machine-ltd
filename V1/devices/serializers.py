from rest_framework import serializers
from V1.devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'sms_number',
        ]
