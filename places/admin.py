from django.contrib import admin, messages
from django.db import DatabaseError, IntegrityError
from .models import PointOfInterest, Place

class PlaceAdmin(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        try:
            return super(PlaceAdmin, self).add_view(request, form_url, extra_context)
        except (IntegrityError, DatabaseError) as e:

            request.method = 'GET'
            messages.error(request, e)
            return super(PlaceAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            return super(PlaceAdmin, self).change_view(request, object_id, form_url, extra_context)
        except (IntegrityError, DatabaseError) as e:

            request.method = 'GET'
            messages.error(request, e)
            return super(PlaceAdmin, self).change_view(request, object_id, form_url, extra_context)

admin.site.register(PointOfInterest)
admin.site.register(Place, PlaceAdmin)
