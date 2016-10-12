from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from .views import PointOfInterestViewSet, PlaceViewSet

router = routers.DefaultRouter()
router.register(r'pois', PointOfInterestViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
