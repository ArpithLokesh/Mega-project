from django.contrib.gis.db import models

class TrafficSignals(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(blank=True, null=True)