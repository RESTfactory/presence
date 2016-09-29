from django.db import models

class Place(models.Model):
    address = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30, blank=True)
    longitude = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
