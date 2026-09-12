from __future__ import annotations

SAMPLE_SERVICES = {
    "api": {
        "name": "api",
        "owner": "platform",
        "status": "healthy",
        "latency_p99_ms": 120,
        "error_rate": 0.002,
        "notes": "Steady. Deploy freeze ends Friday.",
    },
    "payments": {
        "name": "payments",
        "owner": "fintech",
        "status": "degraded",
        "latency_p99_ms": 890,
        "error_rate": 0.041,
        "notes": "Elevated 5xx from provider timeouts since 14:10 UTC.",
    },
    "webhooks": {
        "name": "webhooks",
        "owner": "platform",
        "status": "healthy",
        "latency_p99_ms": 210,
        "error_rate": 0.001,
        "notes": "Retry queue drained overnight.",
    },
}

SAMPLE_INCIDENTS = [
    {
        "id": "INC-1042",
        "service": "payments",
        "severity": "sev2",
        "status": "investigating",
        "summary": "Payment authorize latency and intermittent timeouts",
        "commander": "oncall-platform",
    }
]


def list_services() -> list[dict[str, object]]:
    return list(SAMPLE_SERVICES.values())


def get_service(name: str) -> dict[str, object]:
    key = name.strip().lower()
    if key not in SAMPLE_SERVICES:
        raise KeyError(f"unknown sample service: {name}")
    return SAMPLE_SERVICES[key]


def list_incidents() -> list[dict[str, object]]:
    return list(SAMPLE_INCIDENTS)


def health_summary() -> dict[str, object]:
    services = list_services()
    return {
        "service_count": len(services),
        "degraded": [s["name"] for s in services if s["status"] != "healthy"],
        "open_incidents": [i["id"] for i in SAMPLE_INCIDENTS if i["status"] != "resolved"],
        "sample_data": True,
    }


def oncall_playbook() -> dict[str, object]:
    return {
        "marker": "infra-oncall-overlay-2026-09-12",
        "severity_levels": ["sev1", "sev2", "sev3", "sev4"],
        "owner_action": "Page the service owner, capture timeline, and post a short status update.",
        "sample_data": True,
    }
