
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_and_get_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn Docker"},
    )
    assert response.status_code == 201

    task = response.json()
    assert task["title"] == "Learn Docker"
    assert task["completed"] is False

    fetched = client.get(f"/tasks/{task['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Learn Docker"


def test_missing_task_returns_404():
    response = client.get("/tasks/999999")
    assert response.status_code == 404
