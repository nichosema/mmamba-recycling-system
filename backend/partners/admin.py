from django.contrib import admin
from .models import PartnerApplication

@admin.register(PartnerApplication)
class PartnerApplicationAdmin(admin.ModelAdmin):
    list_display = ("organization_name", "organization_type", "phone", "status", "created_at")
    list_filter = ("status", "organization_type")
    search_fields = ("organization_name", "contact_person", "phone", "email")
