from django.conf import settings
from django.db import models
from places.models import Place

class App(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Entity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    app = models.ForeignKey(App)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Checkin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place)

    def __str__(self):
        return self.name

class Checkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place)

    def __str__(self):
        return self.name
