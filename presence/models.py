from django.conf import settings
# from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import pre_save
from django.core.signals import request_started
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
    place = models.ForeignKey(Place)
    active = models.BooleanField(default=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.created_at)

# Disable all others when creating a session
def session_disabler_handler(sender, instance, *args, **kwargs):
    created = instance.pk != None
    is_active = instance.active

    if(not created):
        place = instance.place
        sessions = place.session_set.filter(active=True)

        for session in sessions:
            session.active = False
            session.save()

    instance.active = is_active

pre_save.connect(session_disabler_handler, sender=Session, dispatch_uid="session_disabler_handler")

class Checkin(DateTimeRegisterMixin):
    session = models.OneToOneField(Session, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    place = models.ForeignKey(Place)

    def __str__(self):
        return str(self.created_at)

class Checkout(DateTimeRegisterMixin):
    session = models.OneToOneField(Session, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    place = models.ForeignKey(Place)

    def __str__(self):
        return str(self.created_at)


# Create a new session if it doesnt come in post, adn auto asociates it to the sender instance
def session_auto_creation_handler(sender, instance, *args, **kwargs):

    if instance.session is None:

        session = Session.objects.create(place=instance.place)
        session.save()

        try:
            instance.session = session
        except Exception as e:
            raise

pre_save.connect(session_auto_creation_handler, sender=Checkin, dispatch_uid="session_auto_creation_handler")
pre_save.connect(session_auto_creation_handler, sender=Checkout, dispatch_uid="session_auto_creation_handler")
