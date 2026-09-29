from decimal import Decimal, InvalidOperation

from rest_framework import status
from rest_framework.response import Response

from .models import Material


def calculate_basket(data):
    """Calculate estimated value for multiple active materials.

    Expected payload:
    {"items": [{"material_id": 1, "weight_kg": 10}, ...]}
    """
    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list) or not items:
        return Response({"detail": "items must be a non-empty list."}, status=status.HTTP_400_BAD_REQUEST)

    results = []
    total = Decimal("0")

    for item in items:
        if not isinstance(item, dict):
            return Response({"detail": "Each item must be an object."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            material_id = int(item.get("material_id"))
            weight = Decimal(str(item.get("weight_kg", "0")))
        except (TypeError, ValueError, InvalidOperation):
            return Response({"detail": "material_id must be an integer and weight_kg must be a valid number."}, status=status.HTTP_400_BAD_REQUEST)

        if weight <= 0:
            return Response({"detail": "weight_kg must be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            material = Material.objects.get(pk=material_id, is_active=True)
        except Material.DoesNotExist:
            return Response({"detail": f"Active material {material_id} was not found."}, status=status.HTTP_404_NOT_FOUND)

        value = weight * material.current_price_per_kg
        total += value
        results.append({
            "material_id": material.id,
            "material": material.name,
            "weight_kg": weight,
            "price_per_kg": material.current_price_per_kg,
            "estimated_value_ugx": value,
        })

    return Response({
        "items": results,
        "total_weight_kg": sum((item["weight_kg"] for item in results), Decimal("0")),
        "estimated_total_ugx": total,
    })
