from utils.api_client import APIClient
from config.config import BASE_URL
def test_get_users():
    client = APIClient()
    response = client.get(
    f"{BASE_URL}/users"
)

    assert response.status_code == 200

    users = response.json()

    assert len(users) > 0
    assert "name" in users[0]
    assert "email" in users[0]
def test_create_user():
    client = APIClient()

    payload = {
        "name": "Naga Silpa",
        "email": "silpa@example.com",
        "username": "silpa"
    }

    response = client.post(
        f"{BASE_URL}/users"
        json=payload
    )

    assert response.status_code == 201

    user = response.json()

    assert user["name"] == "Naga Silpa"
    assert user["email"] == "silpa@example.com"
def test_update_user():
    client = APIClient()

    payload = {
        "name": "Naga Silpa Updated",
        "email": "silpa.updated@example.com",
        "username": "silpa_updated"
    }

    response = client.put(
        "f"{BASE_URL}/users/1",
        json=payload
    )

    assert response.status_code == 200

    user = response.json()

    assert user["name"] == "Naga Silpa Updated"
    assert user["email"] == "silpa.updated@example.com"
def test_delete_user():
    client = APIClient()

    response = client.delete(
        "f"{BASE_URL}/users/1"
    )

    assert response.status_code == 200
def test_update_user():
    client = APIClient()

    payload = {
        "name": "Naga Silpa Updated",
        "email": "silpa.updated@example.com",
        "username": "silpa_updated"
    }

    response = client.put(
        f"{BASE_URL}/users/1",
        json=payload
    )

    assert response.status_code == 200

    user = response.json()

    assert user["name"] == "Naga Silpa Updated"
    assert user["email"] == "silpa.updated@example.com"
    assert user["username"] == "silpa_updated"
def test_get_invalid_user():
    client = APIClient()

    response = client.get(
        f"{BASE_URL}/users/9999"
    )

    assert response.status_code == 404
def test_get_invalid_endpoint():
    client = APIClient()

    response = client.get(
        f"{BASE_URL}/invalid-endpoint"
    )

    assert response.status_code == 404
def test_create_user_response_fields():
    client = APIClient()

    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "username": "testuser"
    }

    response = client.post(
        f"{BASE_URL}/users",
        json=payload
    )

    assert response.status_code == 201

    user = response.json()

    assert "id" in user
    assert user["name"] == "Test User"
    assert user["email"] == "test@example.com"
