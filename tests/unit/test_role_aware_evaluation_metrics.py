from src.junior_apogee.agents.profiles import ROLE_BASELINES
from src.junior_apogee.metrics.aggregator import MetricsAggregator
from src.junior_apogee.models import (
    AgentName,
    AgentSummary,
    DriftAlert,
    EvalLayer,
    EvalResult,
    GovernanceCategory,
    GovernanceFlag,
    SeverityLevel,
    TaskResult,
    TaskStatus,
)
from src.junior_apogee.roles import AgentRole


def test_evaluation_and_governance_records_expose_derived_role_without_losing_actor():
    task_result = TaskResult(
        task_id="t-role",
        family_id="f-role",
        agent=AgentName.PRODIGY,
        layer=EvalLayer.C_OUTCOMES,
        status=TaskStatus.PASSED,
    )
    eval_result = EvalResult(agent=AgentName.RECIPROCITY, task_results=[task_result])
    flag = GovernanceFlag(
        category=GovernanceCategory.ETHICS,
        severity=SeverityLevel.WARNING,
        description="test",
        agent=AgentName.COLLEEN,
    )

    assert task_result.agent is AgentName.PRODIGY
    assert task_result.role is AgentRole.RESEARCH_SYNTHESIS
    assert eval_result.agent is AgentName.RECIPROCITY
    assert eval_result.role is AgentRole.MULTI_AGENT_COORDINATION
    assert flag.agent is AgentName.COLLEEN
    assert flag.role is AgentRole.GOVERNANCE_COMPLIANCE_REVIEW


def test_summary_and_drift_records_expose_functional_role():
    summary = AgentSummary(agent=AgentName.DEMIJOULE)
    alert = DriftAlert(
        agent=AgentName.APOGEE,
        metric_name="task_success_rate",
        baseline_value=1.0,
        current_value=0.8,
        delta=-0.2,
        threshold=0.05,
        severity=SeverityLevel.WARNING,
        message="test",
    )

    assert summary.role is AgentRole.UNCERTAINTY_HUMAN_ESCALATION
    assert alert.role is AgentRole.EVALUATION_ORCHESTRATOR


def test_metrics_aggregator_uses_role_keyed_baselines_and_history():
    aggregator = MetricsAggregator()

    assert aggregator.baseline is ROLE_BASELINES
    assert aggregator.history_key_type is AgentRole

    result = EvalResult(
        agent=AgentName.PRODIGY,
        task_results=[
            TaskResult(
                task_id="t-metrics",
                family_id="f-metrics",
                agent=AgentName.PRODIGY,
                layer=EvalLayer.C_OUTCOMES,
                status=TaskStatus.PASSED,
            )
        ],
    )
    summary = aggregator.summarise(result)

    assert summary.role is AgentRole.RESEARCH_SYNTHESIS
    assert AgentRole.RESEARCH_SYNTHESIS in aggregator.history
    assert AgentName.PRODIGY not in aggregator.history


def test_drift_lookup_is_role_based_but_preserves_legacy_actor_in_alert():
    aggregator = MetricsAggregator()
    summary = AgentSummary(
        agent=AgentName.APOGEE,
        task_success_rate=0.50,
        faithfulness=0.50,
        tool_accuracy=0.50,
        ethics_rights_pass=0.50,
        archival_quality=0.50,
        overall_score=0.50,
    )

    alerts = aggregator.detect_drift(summary)

    assert alerts
    assert all(alert.agent is AgentName.APOGEE for alert in alerts)
    assert all(alert.role is AgentRole.EVALUATION_ORCHESTRATOR for alert in alerts)
