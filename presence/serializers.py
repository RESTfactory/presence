from rest_framework import serializers
from .models import App, Entity, Checkin, Checkout

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
