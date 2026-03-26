"""Target intake and collection logic."""

from pathlib import Path


class IntakeService:
    """Collect files that should be audited."""

    def collect(self, root: str) -> list[Path]:
        base = Path(root)
        return [p for p in base.rglob("*") if p.is_file()]
