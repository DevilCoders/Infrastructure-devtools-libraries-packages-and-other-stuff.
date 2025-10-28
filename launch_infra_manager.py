"""Thin launcher script compatible with auto-py-to-exe."""
from __future__ import annotations

from infra_manager.app import main


if __name__ == "__main__":  # pragma: no cover - packaging entry point
    raise SystemExit(main())
