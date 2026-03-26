"""Read candidate files for scanning."""

from pathlib import Path


class FileReader:
    """Load file contents into memory with basic guards."""

    def read_many(self, paths: list[Path]) -> list[dict]:
        docs: list[dict] = []
        for path in paths:
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            docs.append({"path": str(path), "content": content})
        return docs
