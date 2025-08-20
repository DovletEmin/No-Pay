from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart

@extend_schema(tags=['Order'])
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        cart = Cart.objects.filter(user=self.request.user).first()
        if not cart or not cart.items.exists():
            raise ValidationError({"error": "Корзина пуста"})
        
        order = serializer.save(user=self.request.user, total_price=0)
        total_price = 0 

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            total_price += item.product.price * item.quantity
        
        order.total_price = total_price
        order.save()

        cart.items.all().delete()

        return order
    
    @action(detail=True, methods=["post"])
    def pay(self, request, pk=None):
        order = self.get_object()
        order.status = "paid"
        order.save()

        return Respone({"status": "Оплачен"})