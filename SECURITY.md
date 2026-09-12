# Security Policy

## Reporting a vulnerability

Do **not** open a public GitHub issue for suspected vulnerabilities, exposed credentials, private evaluation data, or exploit details.

Prefer GitHub's private vulnerability-reporting path for this repository when it is enabled. If unavailable, contact the maintainer through a private channel associated with the GitHub account and include only the minimum information required to reproduce the issue. Never place secrets or sensitive career documents in issues, pull requests, screenshots, or logs.

No response-time SLA is promised by this document.

## Current security boundary

This project is an experimental evaluation/QA workbench. Local governance checks, tests, linting, packaging, container builds, or security scanners do not independently establish production security, external compliance, or certification.

Provider credentials such as `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, and application API keys must remain runtime secrets. `.env.example` contains names/placeholders only; real values must not be committed.

Real personal resumes, CVs, application materials, private employer correspondence, or other sensitive career artifacts must not be committed as fixtures or reports. Use synthetic or intentionally sanitized data for repository tests.

## Evidence rule

A green workflow proves only the checks that workflow actually enforced on the bound revision. Advisory/non-blocking scan output must not be reported as a security PASS. Deployment security and provider-side controls require separate evidence.
