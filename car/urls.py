from django.urls import path
from car.views import VehicleList


urlpatterns = [
    path('api/vehicles/', VehicleList.as_view(), name='vehicle-list'),
]