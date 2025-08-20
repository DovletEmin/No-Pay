import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from catalog.models import Category, Product
from cart.models import Cart, CartItem
from orders.models import Order


User = get_user_model()

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create_user(username="orderuser", password="pass123")
    category = Category.objects.create(name="Test Category")
    product = Product.objects.create(name="Prod1", price=20, category=category)
    cart = Cart.objects.create(user=user)
    CartItem.objects.create(cart=cart, product=product, quantity=1)

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post("/api/orders/", {})
    assert response.status_code == 201
    assert Order.objects.filter(user=user).exists()
    order = Order.objects.get(user=user)
    assert order.items.count() == 1


@pytest.mark.django_db
def test_fake_payment():
    user = User.objects.create_user(username="payuser", password="pass123")
    category = Category.objects.create(name="Test Category")
    product = Product.objects.create(name="Prod2", price=30, category=category)
    cart = Cart.objects.create(user=user)
    CartItem.objects.create(cart=cart, product=product, quantity=1)
    
    client = APIClient()
    client.force_authenticate(user=user)
    order_resp = client.post("/api/orders/", {})
    order_id = order_resp.data["id"]
    payment_resp = client.post("/api/payments/charge/", {"order_id": order_id})
    assert payment_resp.status_code == 201
    assert payment_resp.data["status"] in ["success", "failed"]