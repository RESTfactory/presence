from rest_framework import viewsets, status
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from .models import Place
from .serializers import PlaceSerializer

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
