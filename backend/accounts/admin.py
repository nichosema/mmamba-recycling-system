from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class MMAMBAUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("MMAMBA Profile", {"fields": ("role", "phone", "organization_name", "organization_type", "latitude", "longitude")}),
    )
    list_display = ("username", "phone", "role", "organization_name", "is_active")
    list_filter = ("role", "is_active")
