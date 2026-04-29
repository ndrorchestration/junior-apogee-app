# Contributing

> **Governance:** DGAF / Agent Apogee — All changes to this repository are subject to Sentinel CI/CD integrity enforcement. Contributions must pass governance checks before merge. See [DGAF-Framework](https://github.com/Flickerflash/DGAF-Framework) for spine documentation.

## Scope
This repository is the Junior Apogee evaluation and QA workbench — Flask dashboard, layered evaluation logic, governance checks, and reporting scripts for multi-agent system assessment.

## Development
- Keep changes small and reviewable.
- Prefer explicit configuration over hidden defaults.
- Run `python -m pytest tests -v` before pushing evaluation logic changes.
- Validate config YAML files in `config/` before committing.

## Architecture Changes
- New evaluation layers must include unit tests and a corresponding config entry.
- OWASP Agentic Top 10 compliance checks must not be removed or bypassed.

## Pull Requests
- Explain which evaluation layer or governance check is affected.
- Note whether the change affects scoring logic, dashboard routes, or reporting output.
