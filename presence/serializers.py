from rest_framework import serializers
from .models import App, Entity, Session, Checkin, Checkout
from places.serializers import PlaceSerializer

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ["url", "id", "session", "user", "place"]

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ["url", "id", "session", "user", "place"]

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity

class SessionSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    checkin = CheckinSerializer()
    checkout = CheckoutSerializer()

    class Meta:
        model = Session
        fields = ["url", "id", "created_at", "updated_at", "active", "start", "end", "place", "checkin", "checkout"]

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
