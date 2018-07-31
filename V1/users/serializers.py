
from rest_framework import serializers
from V1.devices.serializers import DeviceSerializer
from V1.devices.models import Device
from V1.users.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'devices'
        )
