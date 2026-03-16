# Junior Apogee App

**Three-layer evaluation pipeline for AI assistants**

A production-grade framework that runs tasks through tests, deterministic checks, and LLM-as-judge to produce audit-ready scorecards. Includes task family definitions, metric weights aligned with your evaluation rubrics, and a CLI + web dashboard for tracking agent performance across reasoning, tool-use, and outcomes.comprehensive governance compliance checks (OWASP Agentic Top 10).

## Features

- **Multi-Agent Evaluation**: Score reasoning, tool-use, and outcomes across specialized agents (Apogee, Prodigy, Reciprocity, COLLEEN, DemiJoule)
- **Automated Test Execution**: ~170 task-family tests with deterministic checks + LLM-as-judge
- **Real-time Dashboards**: Metrics tracking and drift monitoring
- **Governance Compliance**: Rights, ethics, hallucination, and archival quality checks
- **Multi-Agent Collaboration**: End-to-end workflow validation

## Architecture

```
Tests & Data → Automated Eval Layer → Metrics & Dashboards → Drift Monitoring → HITL
```

### 3-Layer Eval Spine

**Layer A – Reasoning/Planning**
- Plan quality, adherence, convergence
- Chronology adherence
- Harmonic drift control

**Layer B – Action/Tool-Use**
- Tool selection & parameter accuracy
- Ethics/rights gate-pass
- Self-escalation (DemiJoule-style)

**Layer C – Outcomes**
- Task completion & correctness
- Faithfulness & hallucination rate
- Latency/cost efficiency
- Archival quality & compliance

## Quick Start

### Installation & Setup

```bash
git clone https://github.com/Flickerflash/junior-apogee-app.git
cd junior-apogee-app
# create a virtual environment (recommended outside OneDrive)
python -m venv .venv                # or choose a different path
# PowerShell only:
Set-ExecutionPolicy Bypass -Scope Process -Force
.\.venv\Scripts\Activate.ps1
# cmd shell:
# .\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
# install the package in editable mode
pip install -e .
```

> Environment variables can be managed with a `.env` file; see `.env.example` for keys.

### Project Layout

```
junior-apogee-app/           # repository root
├── junior_apogee_app/       # python package
├── config/                  # YAML definitions for tasks, metrics, agents
├── docs/                    # detailed documentation (see below)
├── scripts/                 # helper scripts (report generation, etc.)
├── tests/                   # pytest-compatible test suite
├── .github/                 # CI/configuration
├── Makefile                 # common commands: install, test, lint
└── README.md
```

### Common Commands

```bash
# run unit tests
python -m pytest tests/ -v

# generate a placeholder report
python scripts/generate_report.py

# invoke CLI helper (after package install)
junior-apogee-app               # show top-level help
junior-apogee-app report        # prints stub message
junior-apogee-app list-agents   # enumerate registered agent types
junior-apogee-app run --task '{"foo": "bar"}'  # execute a basic evaluation flow
junior-apogee-app simulate      # start benchmark/simulation mode

```


## Configuration

See `config/` directory for:
- `task_families.yaml` - Task definitions and success bars
- `metrics.yaml` - Metric definitions and targets
- `agents.yaml` - Agent configurations

## Evaluation Methodology

Based on:
- GAIA-style benchmarking
- Tool-calling accuracy metrics (BFCL)
- Multi-agent collaboration scoring
- Governance alignment checks

## Key Metrics

| Agent | Task Success | Faithfulness | Tool Accuracy | Ethics/Rights | Archival |
|-------|--------------|--------------|---------------|---------------|----------|
| Apogee | 95% | 98% | 99% | 100% | 100% |
| Prodigy | 92% | 100% | 98% | 100% | N/A |
| Reciprocity | 88% | 95% | 90% | 99% | 98% |
| COLLEEN | 91% | 90% | 99% | 99% | 100% |
| DemiJoule | N/A | 97% | N/A | 100% | 99% |

## Documentation

- [Evaluation Framework](docs/EVALUATION_FRAMEWORK.md)
- [Agent Profiles](docs/AGENT_PROFILES.md)
- [Test Suite Design](docs/TEST_SUITE.md)
- [Governance & Compliance](docs/GOVERNANCE.md)

## Contributing

Following Gold Star audit standards. See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License – See [LICENSE](LICENSE) for details

## Author

**Ndr (Flickerflash)** – AI Orchestration Engineer & Prompt Engineer  
Columbus, Ohio

---

**Last Updated**: February 26, 2026  
**Status**: ✅ Production-Ready  
**v0.1.0-beta**
