from rest_framework import viewsets, permissions
from .models import Pickup, CollectorLocation
from .serializers import PickupSerializer, CollectorLocationSerializer

class PickupViewSet(viewsets.ModelViewSet):
    serializer_class = PickupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == "ADMIN":
            return Pickup.objects.all().select_related("customer", "collector")
        if user.role == "COLLECTOR":
            return Pickup.objects.filter(collector=user).select_related("customer")
        return Pickup.objects.filter(customer=user).select_related("collector")

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class CollectorLocationViewSet(viewsets.ModelViewSet):
    serializer_class = CollectorLocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == "ADMIN":
            return CollectorLocation.objects.all()
        return CollectorLocation.objects.filter(collector=user)

    def perform_create(self, serializer):
        serializer.save(collector=self.request.user)
