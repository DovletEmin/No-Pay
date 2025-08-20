from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from orders.models import Order
import random

@extend_schema(tags=['Payment'])
class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        order_id = request.data.get("order_id")
        if not order_id:
            return Response({"detail": "order_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if order.status != "pending":
            return Response({"detail": "Order is already paid or cancelled"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        success = random.choices([True, False], weights=[80, 20])[0]
        status_str = "success" if success else "failed"

        payment = Payment.objects.create(
            order=order,
            amount=order.total_price,
            status=status_str
        )

        if success:
            order.status = "paid"
            order.save()

        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)