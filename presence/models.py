from django.conf import settings
# from django.db import models
from django.contrib.gis.db import models
from places.models import Place

class DateTimeRegisterMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class App(DateTimeRegisterMixin):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Entity(DateTimeRegisterMixin):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    app = models.ForeignKey(App)

    def __str__(self):
        return self.name

class Session(DateTimeRegisterMixin):
    entity = models.ForeignKey(Entity)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return str(self.created_at)

class Checkin(DateTimeRegisterMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    place = models.ForeignKey(Place)

    def __str__(self):
        return str(self.created_at)

class Checkout(DateTimeRegisterMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    place = models.ForeignKey(Place)

    def __str__(self):
        return str(self.created_at)
