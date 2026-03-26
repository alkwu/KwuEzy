"""Rule-based scanning engine."""


class Scanner:
    """Scan loaded documents and emit findings."""

    def scan(self, documents: list[dict]) -> list[dict]:
        findings: list[dict] = []
        for doc in documents:
            if "subprocess" in doc.get("content", ""):
                findings.append(
                    {
                        "path": doc["path"],
                        "rule": "shell_usage",
                        "severity": "medium",
                        "message": "Potential shell execution primitive detected.",
                    }
                )
        return findings
