"""Report formatter."""

from datetime import datetime, timezone


class Reporter:
    """Produce a normalized report payload."""

    def build(self, scored: dict) -> dict:
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "summary": {
                "total_score": scored.get("total_score", 0),
                "finding_count": len(scored.get("findings", [])),
            },
            "findings": scored.get("findings", []),
        }
