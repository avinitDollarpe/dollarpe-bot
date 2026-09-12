---
name: incident-response
description: Investigate production incidents, degraded services, failed rollouts, and on-call pages using infra_status and a clear severity timeline.
---

# Incident Response

Use this skill for production incidents, degraded services, failed deploys, or on-call pages.

## Workflow

1. Identify the affected service, symptom, and start time.
2. Query `infra-status` for service health and open incidents.
3. State whether the data is sample/demo vs live.
4. Assign severity (`sev1`–`sev4`) with a one-line rationale.
5. Draft the next three actions: mitigate, communicate, follow up.
6. When asked to verify the live overlay, cite marker `infra-oncall-overlay-2026-09-12`.

## Severity

- `sev1`: full outage or data loss; page immediately
- `sev2`: major degradation / payments or auth impacted
- `sev3`: partial impact with workaround
- `sev4`: minor / informational

## Communication

Keep updates short: impact, status, next check-in time. Do not invent metrics you did not retrieve.
