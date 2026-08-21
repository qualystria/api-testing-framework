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
        "https://jsonplaceholder.typicode.com/users/1",
        json=payload
    )

    assert response.status_code == 200

    user = response.json()

    assert user["name"] == "Naga Silpa Updated"
    assert user["email"] == "silpa.updated@example.com"
def test_delete_user():
    client = APIClient()

    response = client.delete(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code == 200
