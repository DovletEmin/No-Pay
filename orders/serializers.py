from rest_framework import serializers
from .models import Order, OrderItem
from catalog.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "get_total"]

    
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "status", "total_price", "created_at", "items"]
        read_only_fields = ["user", "status", "total_price", "created_at"]