from rest_framework import serializers
from api.models import Device, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'phone_number',
            'device_id',
        ]

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'sms_number',
        ]
