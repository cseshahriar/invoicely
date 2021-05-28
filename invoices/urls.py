from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import InvoiceViewset, ItemViewset

router = DefaultRouter()
router.register("invoices", InvoiceViewset, basename="invoices")
router.register("items", ItemViewset, basename="items")

urlpatterns = [
    path('', include(router.urls))
]