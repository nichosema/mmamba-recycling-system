from rest_framework import serializers
from .models import PartnerApplication

class PartnerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerApplication
        fields = "__all__"
        read_only_fields = ("status", "reviewed_by", "created_at", "updated_at")
