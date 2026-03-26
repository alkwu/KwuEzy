"""Risk scoring implementation."""


SEVERITY_SCORE = {"low": 1, "medium": 5, "high": 10, "critical": 20}


class RiskScorer:
    """Aggregate finding severities into a single score."""

    def score(self, findings: list[dict]) -> dict:
        total = sum(SEVERITY_SCORE.get(item.get("severity", "low"), 1) for item in findings)
        return {"total_score": total, "findings": findings}
