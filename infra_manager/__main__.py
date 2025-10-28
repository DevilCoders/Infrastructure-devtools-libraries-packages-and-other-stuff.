"""Executable module for ``python -m infra_manager``."""
from __future__ import annotations

from .app import main


if __name__ == "__main__":  # pragma: no cover - entry point
    raise SystemExit(main())
