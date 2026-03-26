from app.core.scorer import RiskScorer


def test_score_defaults_to_zero():
    scorer = RiskScorer()
    result = scorer.score([])
    assert result["total_score"] == 0
