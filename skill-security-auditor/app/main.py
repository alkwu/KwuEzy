"""Entry point for the security auditor service."""

from app.core.intake import IntakeService
from app.core.reader import FileReader
from app.core.scanner import Scanner
from app.core.scorer import RiskScorer
from app.core.reporter import Reporter


def run(path: str) -> dict:
    """Run the end-to-end audit pipeline for a target path."""
    intake = IntakeService()
    reader = FileReader()
    scanner = Scanner()
    scorer = RiskScorer()
    reporter = Reporter()

    targets = intake.collect(path)
    documents = reader.read_many(targets)
    findings = scanner.scan(documents)
    scored = scorer.score(findings)
    return reporter.build(scored)


if __name__ == "__main__":
    import json
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(run(target), indent=2))
