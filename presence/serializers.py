from rest_framework import serializers
from .models import App, Entity, CheckinType, Checkin

class CheckinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckinType

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
