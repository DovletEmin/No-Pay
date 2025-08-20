import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()

    unique_email = f"{uuid.uuid4()}@example.com"  # чтобы email всегда был уникален
    response = client.post("/api/auth/register/", {
        "username": "testuser",
        "email": unique_email,
        "password": "testpass123",
        "password2": "testpass123"
    }, format="json")

    assert response.status_code == 201
    assert User.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_jwt_token():
    user = User.objects.create_user(username="jwtuser", password="testpass123")
    client = APIClient()
    
    response = client.post("/api/token/", {
        "username": "jwtuser",
        "password": "testpass123"
    })

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data