from django.contrib import admin
from .models import Material, PriceHistory

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "current_price_per_kg", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name",)

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ("material", "old_price_per_kg", "new_price_per_kg", "changed_by", "changed_at")
    readonly_fields = ("material", "old_price_per_kg", "new_price_per_kg", "changed_by", "changed_at")
