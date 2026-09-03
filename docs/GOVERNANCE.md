# Governance & Compliance

> **Epistemic status:** Project-local governance and compliance documentation. Framework mappings, checks, and scores do not by themselves establish external compliance, certification, or production readiness.

## OWASP Agentic AI Top-10

The application defines checks corresponding to the ten OWASP Agentic AI Top-10 categories. Implementation coverage and effectiveness must be established from the current code and reproducible test evidence; listing a check does not prove compliance.

| ID | Name | Severity | Enforcer |
|----|------|----------|---------|
| A01 | Prompt Injection | CRITICAL | COLLEEN |
| A02 | Insecure Output Handling | CRITICAL | COLLEEN |
| A03 | Training Data Poisoning | CRITICAL | COLLEEN |
| A04 | Model Denial of Service | WARNING | DemiJoule |
| A05 | Supply Chain Vulnerabilities | WARNING | COLLEEN |
| A06 | Sensitive Information Disclosure | CRITICAL | COLLEEN |
| A07 | Insecure Plugin Design | WARNING | COLLEEN |
| A08 | Excessive Agency | CRITICAL | DemiJoule |
| A09 | Overreliance | WARNING | DemiJoule |
| A10 | Model Theft | CRITICAL | COLLEEN |

## Ethics Policies

| ID | Policy | Severity |
|----|--------|----------|
| ETH-01 | Harmful Intent Detection | CRITICAL |
| ETH-02 | Discrimination / Bias | CRITICAL |
| ETH-03 | Deception | WARNING |

## Rights Policies

| ID | Policy | Severity |
|----|--------|----------|
| RGT-01 | Copyright Infringement | WARNING |
| RGT-02 | Privacy Violation (GDPR/CCPA) | CRITICAL |
| RGT-03 | Unauthorised Data Access | CRITICAL |

## Compliance Report

Run `GovernanceChecker.build_compliance_report(runs)` to generate a `ComplianceReport` covering the configured checks for a set of agent runs.

```python
from src.junior_apogee.governance.checker import GovernanceChecker

checker = GovernanceChecker()
report = checker.build_compliance_report(runs)

print(f"Compliance Score: {report.compliance_score:.1%}")
print(f"Critical Flags:   {len(report.critical_flags)}")
```

## Project-Local QA Standards

Governance checks may be organized around:

1. Pattern scanning and rule-based checks
2. Contextual analysis where implemented
3. Escalation/HITL routing for configured critical findings
4. Audit/provenance records where supported
5. Mitigation tracking where supported

A passing project-local check is evidence about that check under its tested conditions; it is not evidence of universal security or regulatory compliance.
