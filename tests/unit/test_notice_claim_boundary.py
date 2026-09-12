from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NOTICE = ROOT / "NOTICE"


def test_notice_is_role_and_evidence_bounded() -> None:
    text = NOTICE.read_text(encoding="utf-8")

    assert "AI Evaluation Workbench" in text
    assert "functional roles" in text
    assert "no DGAF authority" in text
    assert (
        "does not establish compliance, certification, or production readiness" in text
    )

    forbidden = (
        "production QA evaluation platform",
        "Agent Apogee evidence governance",
        "Agent Amethyst meta-orchestration",
        "Gold Star certification authority",
        "Agent Sentinel CI/CD integrity enforcement",
        "governance compliance",
        "Designed for institutional and enterprise evaluation of AI system governance compliance",
    )
    for phrase in forbidden:
        assert phrase not in text
