from rest_framework import serializers
from V1.locations.models import Location

class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    lat = serializers.FloatField()
    long = serializers.FloatField()
    distance = serializers.FloatField(read_only=True)
    timestamp = serializers.DateTimeField(format="%H:%M:%S %m-%d-%Y", read_only=True)

    class Meta:
        model = Location
        fields = [
            'id',
            'lat',
            'long',
            'distance',
            'timestamp',
        ]
        extra_kwargs = {
            'distance': {'required': False},
            'timestamp': {'required': False}
        }
