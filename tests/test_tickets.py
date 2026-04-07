from fastapi.testclient import TestClient
from app.main import app
from app.db.database import init_db

init_db()
client = TestClient(app)


def test_create_and_get_ticket():
    # Create ticket
    response = client.post("/tickets/", json={
        "title": "CI test ticket",
        "description": "Testing CI"
    })
    assert response.status_code == 200

    # Get tickets
    response = client.get("/tickets/")
    assert response.status_code == 200

    data = response.json()
    assert len(data["tickets"]) > 0
