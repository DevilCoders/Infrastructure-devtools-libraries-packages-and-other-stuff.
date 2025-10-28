"""Performance monitoring panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import PerformanceMetric


class PerformancePanel(QtWidgets.QGroupBox):
    """Render performance telemetry with trend indicators."""

    def __init__(self, metrics: Iterable[PerformanceMetric]) -> None:
        super().__init__("Performance")
        self._metrics = list(metrics)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(len(self._metrics), 4, self)
        self.table.setHorizontalHeaderLabels(["Check", "Value", "Trend", "Status"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        for row, metric in enumerate(self._metrics):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(metric.name))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(metric.value))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(metric.trend))
            status_item = QtWidgets.QTableWidgetItem(metric.status.title())
            status_item.setData(QtCore.Qt.ItemDataRole.UserRole, metric.status)
            self.table.setItem(row, 3, status_item)

        layout.addWidget(self.table)

        self.inspector = QtWidgets.QTextEdit()
        self.inspector.setReadOnly(True)
        self.inspector.setPlaceholderText(
            "Highlight a metric to inspect raw telemetry, flame charts, or profiling hints."
        )
        layout.addWidget(self.inspector)

        self.table.itemSelectionChanged.connect(self._update_inspector)

    # ------------------------------------------------------------------
    def _update_inspector(self) -> None:
        row = self.table.currentRow()
        if row < 0:
            self.inspector.clear()
            return
        metric = self._metrics[row]
        self.inspector.setHtml(
            f"""
            <h3 style='color:#FF0040;'>{metric.name}</h3>
            <p><b>Current:</b> {metric.value}</p>
            <p><b>Trend:</b> {metric.trend}</p>
            <p><b>Status:</b> {metric.status.title()}</p>
            <p>Use this signal to trace regression spikes, compare historical baselines,
            and export flame graphs for deeper introspection.</p>
            """
        )


__all__ = ["PerformancePanel"]
