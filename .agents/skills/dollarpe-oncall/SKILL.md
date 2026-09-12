---
name: dollarpe-oncall
description: DollarPe on-call for Nebula, Nova, Stargate, Horizon, Circuit, Guardian, Orchestrator, Instaramp — incidents, payouts/payin degradation, and status updates.
---

# DollarPe On-call

Use this for DollarPe production incidents across the infra fleet.

## Core services

- **Nebula / Nova** — core APIs
- **Stargate** — payments rail / authorize
- **Horizon** — payin (incl. OwlPay ACH)
- **Circuit** — routing
- **Guardian** — risk / compliance
- **Orchestrator** — workflows
- **Instaramp** — onramp

## Workflow

1. Name the DollarPe service and symptom (authorize fails, ACH pull stuck, KYC block, queue lag).
2. Query `dollarpe-ops` for health + open incidents.
3. Say clearly if data is **sample** vs live.
4. Assign `sev1`–`sev4` with a one-line why.
5. Next actions: mitigate, notify `#dollarpe-incidents` / service channel, schedule next update.
6. Live-overlay proof marker: `dollarpe-bot-overlay-2026-09-12`.

## Severity (DollarPe-flavored)

- `sev1`: payments fully down / funds at risk / data loss
- `sev2`: Stargate/Horizon major degradation, elevated timeout/error rate
- `sev3`: partial impact with workaround (single corridor/provider)
- `sev4`: soft SLO / no customer impact yet (e.g. Orchestrator lag)
