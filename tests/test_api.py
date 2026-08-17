from fastapi.testclient import TestClient

from app.main import create_app, severity


def test_severity_rules() -> None:
    assert severity("ERROR", "database down") == "critical"
    assert severity("WARNING", "queue is growing") == "medium"


def test_logs_are_grouped_into_incidents() -> None:
    with TestClient(create_app()) as client:
        first = client.post(
            "/api/v1/logs", json={"service": "payments", "message": "Timeout id 123"}
        )
        second = client.post(
            "/api/v1/logs", json={"service": "payments", "message": "Timeout id 456"}
        )
    assert first.json()["fingerprint"] == second.json()["fingerprint"]
    assert second.json()["count"] == 2
