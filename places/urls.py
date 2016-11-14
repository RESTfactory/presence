from django.contrib import admin
from rest_framework import routers
from django.conf.urls import (
    url,
    include
)
from .views import (
    PlaceViewSet,
    NearPlacesViewSet
)

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'near', NearPlacesViewSet, base_name="near")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
