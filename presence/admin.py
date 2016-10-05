from django.contrib import admin
from .models import App, Entity, Checkin, Checkout

admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Entity)
admin.site.register(App)
