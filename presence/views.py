from rest_framework import viewsets
from .models import App, Entity, CheckinType, Checkin
from .serializers import AppSerializer, EntitySerializer, CheckinTypeSerializer, CheckinSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class CheckinTypeViewSet(viewsets.ModelViewSet):
    queryset = CheckinType.objects.all()
    serializer_class = CheckinTypeSerializer

class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
