"""Panel showing internal AI model catalogue."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import AIModel


class AIModelPanel(QtWidgets.QWidget):
    """Visualise health and metadata for bespoke AI models."""

    def __init__(self, models: Iterable[AIModel]):
        super().__init__()
        self._models = list(models)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Manage the internally trained foundation models that power the "
            "assistant fleet. Track modality, lifecycle stage, and size in one "
            "place."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        table = QtWidgets.QTableWidget(self)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels([
            "Model",
            "Version",
            "Modality",
            "Status",
            "Parameters",
        ])
        table.horizontalHeader().setStretchLastSection(True)
        table.setRowCount(len(self._models))
        table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.setAlternatingRowColors(True)

        for row, model in enumerate(self._models):
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(model.name))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(model.version))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(model.modality))
            table.setItem(row, 3, QtWidgets.QTableWidgetItem(model.status))
            table.setItem(row, 4, QtWidgets.QTableWidgetItem(model.parameters))

        layout.addWidget(table)

        footer = QtWidgets.QLabel(
            "Models are packaged through the AI orchestrator service and deployed "
            "into GPU backed serving pools. Use the automation tab to trigger "
            "refreshes or canary promotions."
        )
        footer.setWordWrap(True)
        footer.setStyleSheet("color: #C0C0C0;")
        layout.addWidget(footer)


__all__ = ["AIModelPanel"]
