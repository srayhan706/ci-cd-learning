from fastapi.testclient import TestClient

from app import add, app, multipication, subtract

client = TestClient(app)


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multipication():
    assert multipication(4, 5) == 20


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_add_route():
    resp = client.get("/add/2/3")
    assert resp.json()["result"] == 5
