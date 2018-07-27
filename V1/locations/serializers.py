from rest_framework import serializers
from V1.locations.models import Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            'id',
            'lat',
            'long',
            'distance',
            'timestamp',
        ]
