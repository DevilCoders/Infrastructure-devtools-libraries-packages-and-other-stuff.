"""Operational runbook panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import Runbook


class RunbookPanel(QtWidgets.QWidget):
    """Showcase curated incident and maintenance runbooks."""

    def __init__(self, runbooks: Iterable[Runbook]):
        super().__init__()
        self._runbooks = list(runbooks)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Runbook", "Trigger", "Steps", "Severity"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for runbook in self._runbooks:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [runbook.name, runbook.trigger, str(runbook.steps), runbook.severity]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["RunbookPanel"]
