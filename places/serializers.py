from rest_framework import serializers
from .models import (
    Place
)

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["url", "id", "place_id", "address", "name", "latitude", "longitude", "code", "point"]
