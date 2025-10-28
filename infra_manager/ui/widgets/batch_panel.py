"""Bulk and batch processing panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import BatchProcess


class BatchPanel(QtWidgets.QWidget):
    """Simulate bulk processing waves."""

    def __init__(self, processes: Iterable[BatchProcess]):
        super().__init__()
        self._processes = {proc.name: proc for proc in processes}
        self._active_timer: QtCore.QTimer | None = None
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        label = QtWidgets.QLabel(
            "Coordinate infrastructure wide batch jobs with a unified progress tracker."
        )
        label.setWordWrap(True)
        layout.addWidget(label)

        self._table = QtWidgets.QTableWidget(len(self._processes), 4, self)
        self._table.setHorizontalHeaderLabels(["Process", "Items", "Status", "Progress"])
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        for row, process in enumerate(self._processes.values()):
            self._table.setItem(row, 0, QtWidgets.QTableWidgetItem(process.name))
            self._table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(process.items)))
            self._table.setItem(row, 2, QtWidgets.QTableWidgetItem(process.status))
            bar = QtWidgets.QProgressBar(self)
            bar.setValue(0 if process.status != "running" else 40)
            self._table.setCellWidget(row, 3, bar)

        layout.addWidget(self._table)

        controls = QtWidgets.QHBoxLayout()
        self._start_button = QtWidgets.QPushButton("Process Batch", self)
        self._start_button.clicked.connect(self._start_batch)
        controls.addWidget(self._start_button)
        controls.addStretch(1)
        layout.addLayout(controls)

        self._status = QtWidgets.QLabel("Awaiting selection")
        layout.addWidget(self._status)

    def _start_batch(self) -> None:
        row = self._table.currentRow()
        if row < 0:
            self._status.setText("Select a batch process to execute")
            return
        name = self._table.item(row, 0).text()
        process = self._processes[name]
        process.status = "running"
        status_item = self._table.item(row, 2)
        if status_item:
            status_item.setText(process.status)
        bar = self._table.cellWidget(row, 3)
        if isinstance(bar, QtWidgets.QProgressBar):
            bar.setValue(0)

        if self._active_timer:
            self._active_timer.stop()

        timer = QtCore.QTimer(self)
        timer.setInterval(200)
        progress = {"value": 0}

        def advance() -> None:
            progress["value"] += 10
            bar_local = self._table.cellWidget(row, 3)
            if isinstance(bar_local, QtWidgets.QProgressBar):
                bar_local.setValue(min(progress["value"], 100))
            if progress["value"] >= 100:
                timer.stop()
                process.status = "complete"
                status_item_local = self._table.item(row, 2)
                if status_item_local:
                    status_item_local.setText(process.status)
                self._status.setText(f"{name} complete")

        timer.timeout.connect(advance)
        timer.start()
        self._active_timer = timer
        self._status.setText(f"Processing {name}")


__all__ = ["BatchPanel"]
