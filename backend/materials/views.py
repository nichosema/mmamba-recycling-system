from decimal import Decimal
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Material, PriceHistory
from .serializers import MaterialSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve", "calculate"):
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

    @action(detail=True, methods=["post"], url_path="calculate")
    def calculate(self, request, pk=None):
        material = self.get_object()
        try:
            weight = Decimal(str(request.data.get("weight_kg", "0")))
        except Exception:
            return Response({"detail": "weight_kg must be a valid number."}, status=400)
        if weight <= 0:
            return Response({"detail": "weight_kg must be greater than zero."}, status=400)
        total = weight * material.current_price_per_kg
        return Response({
            "material": material.name,
            "weight_kg": weight,
            "price_per_kg": material.current_price_per_kg,
            "estimated_value_ugx": total,
        })
