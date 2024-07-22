from django.contrib import admin

from car.models import Brand, Vehicle


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = "id", "name", "model", "created", "updated"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = "id", "number", "created", "updated"
