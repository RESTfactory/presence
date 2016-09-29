from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from .views import PlaceViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
