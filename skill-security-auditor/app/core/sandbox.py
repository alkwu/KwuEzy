"""Sandbox execution helpers."""


class Sandbox:
    """Stub for executing untrusted checks in isolation."""

    def run(self, payload: str) -> dict:
        return {"status": "not_implemented", "payload_size": len(payload)}
