from django.contrib import admin
from .models import App, Entity, CheckinType, Checkin

admin.site.register(CheckinType)
admin.site.register(Checkin)
admin.site.register(Entity)
admin.site.register(App)
