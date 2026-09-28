from rest_framework import serializers
from .models import Pickup, CollectionItem, CollectorLocation

class CollectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItem
        fields = "__all__"
        read_only_fields = ("total_value",)

class PickupSerializer(serializers.ModelSerializer):
    items = CollectionItemSerializer(many=True, read_only=True)
    class Meta:
        model = Pickup
        fields = "__all__"
        read_only_fields = ("customer", "requested_at")

class CollectorLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectorLocation
        fields = "__all__"
        read_only_fields = ("collector", "recorded_at")
