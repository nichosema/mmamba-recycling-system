from rest_framework import viewsets, permissions
from .models import PartnerApplication
from .serializers import PartnerApplicationSerializer

class PartnerApplicationViewSet(viewsets.ModelViewSet):
    queryset = PartnerApplication.objects.all().order_by("-created_at")
    serializer_class = PartnerApplicationSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def perform_update(self, serializer):
        serializer.save(reviewed_by=self.request.user)
