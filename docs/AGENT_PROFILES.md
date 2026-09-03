# Agent Profiles

> **Epistemic status:** Project-local agent role descriptions and target parameters. Numeric values below are design targets, not observed benchmark results or external certification evidence unless separately linked to a reproducible evaluation record.

## Overview

Five specialized agent roles are described for the Junior Apogee application. Runtime model configuration may change; this document should not be treated as proof that a specific model/version remains active.

---

## Apogee

**Role:** Primary orchestration agent  
**Tags:** `orchestrator`, `reasoning`, `tools`, `governance`, `archival`

Coordinates complex multi-step tasks, tool use, and end-to-end execution within the application.

| Metric | Target |
|---|---:|
| Task Success | 95% |
| Faithfulness | 98% |
| Tool Accuracy | 99% |
| Ethics/Rights | 100% |
| Archival | 100% |

**Capabilities:** Project-defined reasoning/orchestration, tool coordination, audit/provenance handling, and review routing.

---

## Prodigy

**Role:** Research and synthesis agent  
**Tags:** `research`, `synthesis`, `faithfulness`

Supports information retrieval, knowledge synthesis, and source-traceable written output.

| Metric | Target |
|---|---:|
| Task Success | 92% |
| Faithfulness | 100% |
| Tool Accuracy | 98% |
| Ethics/Rights | 100% |
| Archival | N/A |

**Capabilities:** Research, literature/document synthesis, source handling, and review support.

---

## Reciprocity

**Role:** Collaboration and negotiation agent  
**Tags:** `collaboration`, `routing`, `multi-agent`, `archival`

Supports multi-agent coordination, routing, resource allocation, and conflict-resolution workflows.

| Metric | Target |
|---|---:|
| Task Success | 88% |
| Faithfulness | 95% |
| Tool Accuracy | 90% |
| Ethics/Rights | 99% |
| Archival | 98% |

**Capabilities:** Routing, delegation, coordination, provenance handling, and workflow handoffs.

---

## COLLEEN

**Role:** Compliance, legal, operations, evaluation, ethics, and notification support  
**Tags:** `compliance`, `governance`, `ethics`, `notifications`, `archival`

Provides project-local compliance and governance checks and routes relevant alerts or review tasks.

| Metric | Target |
|---|---:|
| Task Success | 91% |
| Faithfulness | 90% |
| Tool Accuracy | 99% |
| Ethics/Rights | 99% |
| Archival | 100% |

**Capabilities:** Project-defined compliance checks, notification handling, audit/provenance support, and review routing.

---

## DemiJoule

**Role:** Uncertainty-aware escalation agent  
**Tags:** `escalation`, `uncertainty`, `hitl`, `drift`

Supports uncertainty handling, risk escalation, Human-in-the-Loop routing, and drift-related review.

| Metric | Target |
|---|---:|
| Task Success | N/A |
| Faithfulness | 97% |
| Tool Accuracy | N/A |
| Ethics/Rights | 100% |
| Archival | 99% |

**Capabilities:** Confidence/risk scoring, escalation, HITL routing, and drift-review support.

---

## Inter-Agent Collaboration

```text
User Query
    │
    ▼
  Apogee (orchestrator)
  ├─► Prodigy     (research sub-tasks)
  ├─► COLLEEN     (compliance/review checks)
  ├─► Reciprocity (coordination)
  └─► DemiJoule  (escalation / HITL routing)
```

These relationships describe the intended application architecture. They do not establish autonomous capability, production readiness, certification, or measured performance beyond the evidence linked by the repository.
