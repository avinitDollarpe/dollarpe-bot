from __future__ import annotations

# Sample fleet shaped like Desktop/dollarpe-infra services.
# Explicitly sample_data until live systems are wired.
SAMPLE_SERVICES = {
    "nebula": {
        "name": "Nebula",
        "stack": "core-api",
        "owner": "platform",
        "status": "healthy",
        "notes": "Primary API surface steady.",
    },
    "nova": {
        "name": "Nova",
        "stack": "core-api",
        "owner": "platform",
        "status": "healthy",
        "notes": "Companion API healthy.",
    },
    "stargate": {
        "name": "Stargate",
        "stack": "payments-rail",
        "owner": "payments",
        "status": "degraded",
        "notes": "Elevated provider timeouts on authorize path since 14:10 UTC.",
    },
    "horizon": {
        "name": "Horizon",
        "stack": "payin",
        "owner": "payments",
        "status": "healthy",
        "notes": "OwlPay ACH pull path nominal.",
    },
    "circuit": {
        "name": "Circuit",
        "stack": "routing",
        "owner": "platform",
        "status": "healthy",
        "notes": "Route table synced.",
    },
    "guardian": {
        "name": "Guardian",
        "stack": "risk-compliance",
        "owner": "risk",
        "status": "healthy",
        "notes": "Policy checks green.",
    },
    "orchestrator": {
        "name": "Orchestrator",
        "stack": "workflow",
        "owner": "platform",
        "status": "yellow",
        "notes": "Queue lag above soft SLO; no customer impact yet.",
    },
    "instaramp": {
        "name": "Instaramp",
        "stack": "onramp",
        "owner": "product",
        "status": "healthy",
        "notes": "Onramp UI/API healthy.",
    },
}

SAMPLE_INCIDENTS = [
    {
        "id": "DP-INC-214",
        "service": "Stargate",
        "severity": "sev2",
        "status": "investigating",
        "summary": "Stargate authorize latency / intermittent provider timeouts",
        "commander": "payments-oncall",
        "channels": ["#dollarpe-incidents", "#payments"],
    }
]


def list_services() -> list[dict[str, object]]:
    return list(SAMPLE_SERVICES.values())


def get_service(name: str) -> dict[str, object]:
    key = name.strip().lower()
    if key not in SAMPLE_SERVICES:
        raise KeyError(f"unknown DollarPe sample service: {name}")
    return SAMPLE_SERVICES[key]


def list_incidents() -> list[dict[str, object]]:
    return list(SAMPLE_INCIDENTS)


def health_summary() -> dict[str, object]:
    services = list_services()
    return {
        "org": "DollarPe",
        "bot": "dollarpe-bot",
        "service_count": len(services),
        "degraded": [s["name"] for s in services if s["status"] not in {"healthy"}],
        "open_incidents": [i["id"] for i in SAMPLE_INCIDENTS if i["status"] != "resolved"],
        "sample_data": True,
    }


def oncall_playbook() -> dict[str, object]:
    return {
        "org": "DollarPe",
        "bot": "dollarpe-bot",
        "marker": "dollarpe-bot-overlay-2026-09-12",
        "severity_levels": ["sev1", "sev2", "sev3", "sev4"],
        "owner_action": "Page payments/platform oncall, capture timeline in #dollarpe-incidents, post customer-safe status.",
        "sample_data": True,
    }
