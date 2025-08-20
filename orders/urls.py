from django.urls import path
from .views import OrderViewSet

urlpatterns = [
    path('', OrderViewSet.as_view({"get": "list", "post": "create"}), name="orders"),
    path("<int:pk>/", OrderViewSet.as_view({"get": "retrieve"}), name="order-detail"),
    path("<int:pk>/pay/", OrderViewSet.as_view({"post": "pay"}), name="order-pay"),
]