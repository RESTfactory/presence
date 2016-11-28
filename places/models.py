from django.contrib.gis.geos import Point
from django.contrib.gis.db import models
from django.db.models.signals import pre_save
from geopy.geocoders import Nominatim

class PlaceMarkerMixin(models.Model):
    place_id = models.IntegerField(unique=True, blank=True, null=True, editable=False)
    address = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)

    class Meta:
        abstract = True

class Place(PlaceMarkerMixin):
    code = models.CharField(max_length=40, unique=True)

    point = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    def __str__(self):
        return self.address

def place_handler(sender, instance, *args, **kwargs):
    geolocator = Nominatim()
    location = None

    if(instance.latitude == "-"):
        instance.latitude = None;

    if(instance.longitude == "-"):
        instance.longitude = None;

    if(not instance.address):
        if(instance.latitude and instance.longitude):
            location = geolocator.reverse("%s, %s" % (instance.latitude, instance.longitude), timeout=10)

            place_id = location.raw.get("place_id")

            instance.place_id = place_id
            instance.address = location.address
            instance.point = Point(location.longitude, location.latitude)

    if(instance.latitude and instance.longitude):
        instance.point = Point(float(instance.longitude), float(instance.latitude))

pre_save.connect(place_handler, sender=Place, dispatch_uid="place_handler")
