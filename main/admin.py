from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import TrafficSignals


@admin.register(TrafficSignals)
class TrafficAdmin(OSMGeoAdmin):
    list_display = ("name", "location")