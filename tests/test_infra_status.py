from tools.infra_status import client


def test_health_summary_marks_sample_data():
    summary = client.health_summary()
    assert summary["sample_data"] is True
    assert "payments" in summary["degraded"]


def test_get_service():
    svc = client.get_service("api")
    assert svc["status"] == "healthy"
