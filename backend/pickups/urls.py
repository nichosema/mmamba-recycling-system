from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PickupViewSet, CollectorLocationViewSet

router = DefaultRouter()
router.register("requests", PickupViewSet, basename="pickup")
router.register("locations", CollectorLocationViewSet, basename="collector-location")

urlpatterns = [path("", include(router.urls))]
