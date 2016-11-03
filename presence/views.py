from rest_framework import viewsets
from .models import App, Entity, Session, Checkin, Checkout
from .serializers import AppSerializer, EntitySerializer, SessionSerializer, CheckinSerializer, CheckoutSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all().order_by('-created_at')
    serializer_class = CheckinSerializer

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all().order_by('-created_at')
    serializer_class = CheckoutSerializer
