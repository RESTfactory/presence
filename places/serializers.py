from rest_framework import serializers
from .models import PointOfInterest, Place

class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
