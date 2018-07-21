from rest_framework import serializers
from api.models import User, Device

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'phone_number',
            'device_number',
            'redius'
        ]

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'sms_number',
            'location_1',
            'location_2',
            'location_3',
        ]
