from rest_framework import generics
from car.models import Vehicle
from car.serializers import VehicleSerializer


class VehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
