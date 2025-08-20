from django.urls import path
from .views import PaymentViewSet

urlpatterns = [
    path("charge/", PaymentViewSet.as_view({"post": "create"}), name="payment-charge")
]