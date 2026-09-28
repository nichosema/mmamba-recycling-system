from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PartnerApplicationViewSet

router = DefaultRouter()
router.register("applications", PartnerApplicationViewSet, basename="partner-application")

urlpatterns = [path("", include(router.urls))]
