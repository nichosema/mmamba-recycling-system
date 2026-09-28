from django.conf import settings
from django.db import models
from materials.models import Material

class Pickup(models.Model):
    class Status(models.TextChoices):
        REQUESTED = "REQUESTED", "Requested"
        ASSIGNED = "ASSIGNED", "Assigned"
        ON_THE_WAY = "ON_THE_WAY", "On the way"
        ARRIVED = "ARRIVED", "Arrived"
        COLLECTED = "COLLECTED", "Collected"
        CANCELLED = "CANCELLED", "Cancelled"

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="pickups")
    collector = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name="assigned_pickups")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REQUESTED)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=500, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

class CollectionItem(models.Model):
    pickup = models.ForeignKey(Pickup, on_delete=models.CASCADE, related_name="items")
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    verified_weight_kg = models.DecimalField(max_digits=12, decimal_places=3)
    price_per_kg = models.DecimalField(max_digits=12, decimal_places=2)
    total_value = models.DecimalField(max_digits=14, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_value = self.verified_weight_kg * self.price_per_kg
        super().save(*args, **kwargs)

class CollectorLocation(models.Model):
    collector = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="locations")
    pickup = models.ForeignKey(Pickup, on_delete=models.SET_NULL, null=True, blank=True, related_name="locations")
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]
