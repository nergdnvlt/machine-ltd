from rest_framework import serializers
from api.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'location_1',
            'location_2',
            'location_3',
            'location_4',
            'location_5',
        ]
