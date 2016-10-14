from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D as distance
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from .models import PointOfInterest, Place
from .serializers import PointOfInterestSerializer, PlaceSerializer

class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def create(self, request, *args, **kwargs):
        try:
            place = None

            # Validate if place exists!
            try:
                geolocator = Nominatim()
                location = None

                location = geolocator.reverse("%s, %s" % (request.data.get("latitude"), request.data.get("longitude")), timeout=10)
                place_id = location.raw.get("place_id")

                old_place = Place.objects.get(place_id=place_id)

                if(old_place):
                    serializer = self.get_serializer(old_place)
                    return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                pass

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            return Response({"msg":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class NearPlacesViewSet(viewsets.ViewSet):

    def create(self, request):
        latitude = float(request.data.get("latitude"))
        longitude = float(request.data.get("longitude"))

        current_location = Point(longitude, latitude)
        places = Place.objects.filter(point__distance_lte=(current_location, distance(m=100)))

        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
