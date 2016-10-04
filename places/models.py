from django.db import models
from django.db.models.signals import pre_save
from geopy.geocoders import Nominatim

class Place(models.Model):
    address = models.CharField(max_length=30, blank=True)
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
            instance.address = location.address

pre_save.connect(place_handler, sender=Place, dispatch_uid="place_handler")
