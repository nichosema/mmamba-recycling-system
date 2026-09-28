from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "phone", "role", "organization_name", "organization_type", "latitude", "longitude")
        read_only_fields = ("id", "role")

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email", "phone")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
