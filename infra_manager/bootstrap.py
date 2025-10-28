"""Bootstrap helpers for the Qt application."""
from __future__ import annotations

from PyQt6 import QtCore


def configure_qt_attributes() -> None:
    """Configure high-DPI and rendering attributes before the app starts."""

    QtCore.QCoreApplication.setAttribute(
        QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True
    )
    QtCore.QCoreApplication.setAttribute(
        QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True
    )


__all__ = ["configure_qt_attributes"]
