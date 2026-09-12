# AI Evaluation Workbench — Working Title

![Status](https://img.shields.io/badge/Status-Experimental-blue)
![Language](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)

> **Epistemic status:** Experimental evaluation and QA workbench. The repository implements local evaluation workflows and governance-related checks; it does not by itself establish external certification, compliance, or production readiness.

This project is an evidence-native evaluation and QA workbench for AI and multi-agent systems. It includes a Flask dashboard, layered evaluation logic, governance-related checks, reporting scripts, and local experimentation workflows.

## Naming status

The former product and agent proper-name family is **deprecated for current use**. Those names may still appear in the repository slug, Python package/import paths, historical records, compatibility shims, immutable evidence, and migration documentation until a final product brand and technical migration are completed.

Do not use the retired proper name as a current product, agent, persona, authority, or marketing identity. Preserve useful former persona/role characteristics only as functional responsibilities such as verification, evidence governance, bounded scoring, provenance review, integrity checks, and escalation support.

## Scope and boundaries

The active implementation lives in `src/junior_apogee/`, with the dashboard entry point at the repository root in `app.py`. The existing package path is a temporary compatibility identifier, not the current product name.

The top-level `junior_apogee_app/` package remains for older examples and tests; new work should target the `src/` implementation until the final technical rename is planned and executed.

Historical DGAF protocol numbers, retired agent-role labels, harmonic parameters, and prior governance anchors are provenance/context only unless a current canonical record explicitly re-establishes them for a present-tense claim.

## What Is In This Repo

- `app.py` — dashboard backend and demo API routes
- `src/junior_apogee/` — current implementation package; legacy technical identifier pending final rename
- `config/` — YAML definitions for agents, metrics, and task families
- `scripts/run_eval.py` — pytest wrapper for running subsets of the suite
- `scripts/generate_report.py` — synthetic report generator
- `tests/` — unit, integration, and legacy compatibility tests

## Quick Start

```bash
git clone https://github.com/ndrorchestration/junior-apogee-app.git
cd junior-apogee-app
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

## Run Tests

```bash
python -m pytest tests -v
```

Or:

```bash
python scripts/run_eval.py --layer all -v
```

## Generate a Sample Report

```bash
python scripts/generate_report.py --tasks 5 --output reports/report.json
```

## Package Smoke Check

```bash
python -m junior_apogee info
```

The package command above is retained temporarily for compatibility and does not represent the current product name.

## Configuration

- Copy `.env.example` to `.env` for local environment variables.
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` enables LLM-judge features.
- YAML configuration lives in `config/agents.yaml`, `config/metrics.yaml`, and `config/task_families.yaml`.

API keys enable integrations; their presence does not constitute evaluation validation.

## Docker

```bash
docker build -t junior-apogee-app .
docker run -p 5000:5000 junior-apogee-app
```

The image tag above is a temporary compatibility identifier. There is currently no `docker-compose.yml` in the repository.

## Related Ecosystem

- `DGAF-Framework` — related governance/evaluation research track
- `resumeapex-eval` — separate benchmark/evaluation track
- `Driftwatch` — separate drift-detection track
- `sentinel-governance` — separate CI/integrity track
- `Amethyst-Governance-Eval-Stack` — related evaluation/orchestration track
- `Gold-star-standards` — related internal rubric/standards artifacts
- `3d-visualization-hub` — visualization companion

Cross-repository relationships do not establish mutual validation or certification.

## Epistemic Standard

Use the following distinction when documenting results:

**DEFINED → IMPLEMENTED → COMPUTED → VERIFIED → ATTESTED → HISTORICAL → HYPOTHESIS → METAPHOR → UNSUPPORTED → DEPRECATED**

A local test demonstrates the behavior tested under those conditions. It does not automatically establish general reliability, external compliance, or certification.

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.

## Provenance

Developed by Ndr / Ender Hensel (`ndrorchestration`).
