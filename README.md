## Quick Overview (In Plain Language)

This project is a small “test bench” for AI systems.

In simple terms:
- You give an AI a task (for example: answer a question or summarize text).
- This project runs the AI through that task in a controlled way.
- It records what happened so you can see how well the AI behaved or where it failed.

Right now this is an early **v0.1** version:
- It’s focused on showing my thinking and structure.
- Some parts are still work-in-progress or stubs.
- You can still read the layout and comments to see how I design and evaluate AI behavior.

# Junior Apogee App

**Production-ready AI agent evaluation and QA platform**

Built on a 3-layer evaluation spine aligned with 2025–26 agentic AI best practices. Multi-agent scoring, automated testing, real-time dashboards, and comprehensive governance compliance checks (OWASP Agentic Top 10).

## Features

- **Multi-Agent Evaluation**: Score reasoning, tool-use, and outcomes across specialized agents (Apogee, Prodigy, Reciprocity, COLLEEN, DemiJoule).
- **Automated Test Execution**: ~170 task-family tests with deterministic checks + LLM-as-judge.
- **Real-time Dashboards**: Metrics tracking and drift monitoring.
- **Governance Compliance**: Rights, ethics, hallucination, and archival quality checks.
- **Multi-Agent Collaboration**: End-to-end workflow validation.

## Architecture

```text
Tests & Data → Automated Eval Layer → Metrics & Dashboards → Drift Monitoring → HITL


## 5-Minute Quick Start

Get Junior Apogee running and execute your first evaluation in < 5 minutes:

### Step 1: Install
```bash
git clone https://github.com/Flickerflash/junior-apogee-app.git
cd junior-apogee-app
pip install -r requirements.txt
```

### Step 2: Configure
Copy `.env.example` to `.env` and set your LLM API key (OpenAI, Anthropic, or local).

### Step 3: Run an Evaluation
```bash
python app.py --config configs/example_eval.json
```

This executes a sample evaluation task and outputs results to `results/sample_results.json`.

For Docker: `docker-compose up --build` or `docker run -e API_KEY=<your-key> flickerflash/junior-apogee:latest`

---

## Docker & Deployment

**Docker**: Pre-built image available for cloud deployment.

```bash
docker build -t junior-apogee .
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY junior-apogee
```

**Docker Compose**: For local development with services.

```bash
docker-compose -f docker-compose.yml up
```

See `Dockerfile` and `docker-compose.yml` for full configuration.

---

## Example Evaluation Config

See `configs/example_eval.json` for a sample evaluation specification:

```json
{
  "name": "Agent Reasoning Test",
  "task": "answer_question",
  "input": "What are the main causes of climate change?",
  "agents": ["Apogee", "Prodigy"],
  "metrics": ["accuracy", "coherence", "bias"],
  "threshold": 0.8
}
```

Sample results are available in `results/sample_results.json` showing:
- Per-agent scores (reasoning, tool-use, outcomes)
- Compliance checks (OWASP Agentic Top 10)
- Drift monitoring and trend analysis
- HITL (Human-in-the-Loop) review flags
