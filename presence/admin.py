from django.contrib import admin
from .models import App, Entity, Session, Checkin, Checkout

admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Entity)
admin.site.register(Session)
admin.site.register(App)
