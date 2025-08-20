import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from catalog.models import Category, Product


User = get_user_model()

@pytest.mark.django_db
def test_add_to_cart():
    user = User.objects.create_user(username="cartuser", password="pass123")
    category = Category.objects.create(name="Test Category")
    product = Product.objects.create(name="Test Project", price=10, category=category)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post("/api/cart/", {
        "product_id": product.id,
        "quantity": 2
    }, format="json")
    assert response.status_code == 201
    assert response.data["quantity"] == 2