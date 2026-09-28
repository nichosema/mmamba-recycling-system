from rest_framework import viewsets, permissions
from .models import Material, PriceHistory
from .serializers import MaterialSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def perform_update(self, serializer):
        material = self.get_object()
        old_price = material.current_price_per_kg
        updated = serializer.save()
        if old_price != updated.current_price_per_kg:
            PriceHistory.objects.create(
                material=updated,
                old_price_per_kg=old_price,
                new_price_per_kg=updated.current_price_per_kg,
                changed_by=self.request.user,
            )
