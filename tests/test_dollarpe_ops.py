from tools.dollarpe_ops import client


def test_health_summary_is_dollarpe():
    summary = client.health_summary()
    assert summary["org"] == "DollarPe"
    assert summary["bot"] == "dollarpe-bot"
    assert summary["sample_data"] is True
    assert "Stargate" in summary["degraded"]


def test_get_stargate():
    svc = client.get_service("stargate")
    assert svc["stack"] == "payments-rail"
