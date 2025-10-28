"""Access governance panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import AccessProfile


class AccessPanel(QtWidgets.QWidget):
    """Summarise access profiles and status."""

    def __init__(self, profiles: Iterable[AccessProfile]):
        super().__init__()
        self._profiles = list(profiles)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        blurb = QtWidgets.QLabel(
            "Guard environment privileges with curated access packages."
        )
        blurb.setWordWrap(True)
        layout.addWidget(blurb)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Profile", "Scope", "Description", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for profile in self._profiles:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [profile.name, profile.scope, profile.description, profile.status]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["AccessPanel"]
