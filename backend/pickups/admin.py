from django.contrib import admin
from .models import Pickup, CollectionItem, CollectorLocation

class CollectionItemInline(admin.TabularInline):
    model = CollectionItem
    extra = 0

@admin.register(Pickup)
class PickupAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "collector", "status", "scheduled_for", "requested_at")
    list_filter = ("status",)
    search_fields = ("customer__username", "customer__phone", "address")
    inlines = [CollectionItemInline]

@admin.register(CollectorLocation)
class CollectorLocationAdmin(admin.ModelAdmin):
    list_display = ("collector", "pickup", "latitude", "longitude", "recorded_at")
    list_filter = ("collector",)
