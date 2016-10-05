from rest_framework import viewsets
from .models import App, Entity, Checkin, Checkout
from .serializers import AppSerializer, EntitySerializer, CheckinSerializer, CheckoutSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all().order_by('-created_at')
    serializer_class = CheckinSerializer

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all().order_by('-created_at')
    serializer_class = CheckoutSerializer
