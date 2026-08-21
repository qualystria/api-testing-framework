import requests


def test_get_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10
    )

    assert response.status_code == 200

    users = response.json()

    assert len(users) > 0
    assert "name" in users[0]
    assert "email" in users[0]
