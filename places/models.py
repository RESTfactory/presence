from django.db import models
from django.db.models.signals import pre_save
from geopy.geocoders import Nominatim

class Place(models.Model):
    place_id = models.IntegerField(unique=True, blank=True, editable=False)
    address = models.CharField(max_length=255, blank=True, editable=False)
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.address

def place_handler(sender, instance, *args, **kwargs):
    geolocator = Nominatim()
    location = None

    if(not instance.address):
        if(instance.latitude and instance.longitude):
            location = geolocator.reverse("%s, %s" % (instance.latitude, instance.longitude), timeout=10)

            place_id = location.raw.get("place_id")

            instance.place_id = place_id
            instance.address = location.address

pre_save.connect(place_handler, sender=Place, dispatch_uid="place_handler")
