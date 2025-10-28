"""Asynchronous job orchestrator panel."""
from __future__ import annotations

import time
from typing import Dict, Iterable

from PySide6 import QtCore, QtWidgets

from ...core.state import AsyncJob


class JobSignals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    finished = QtCore.Signal(str)


class JobRunner(QtCore.QRunnable):
    """Execute a simulated asynchronous job."""

    def __init__(self, job: AsyncJob):
        super().__init__()
        self.job = job
        self.signals = JobSignals()

    @QtCore.Slot()
    def run(self) -> None:
        self.job.status = "running"
        for pct in range(self.job.progress, 101, 20):
            time.sleep(0.25)
            self.signals.progress.emit(self.job.name, pct)
        self.signals.finished.emit(self.job.name)


class AsyncJobsPanel(QtWidgets.QWidget):
    """Manage asyncio and multithreaded jobs."""

    def __init__(self, jobs: Iterable[AsyncJob]):
        super().__init__()
        self._jobs = {job.name: job for job in jobs}
        self._row_index: Dict[str, int] = {}
        self._thread_pool = QtCore.QThreadPool.globalInstance()
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        headline = QtWidgets.QLabel(
            "Schedule async tasks, multithreaded fan-outs, and monitor progress."
        )
        headline.setWordWrap(True)
        layout.addWidget(headline)

        self._table = QtWidgets.QTableWidget(len(self._jobs), 4, self)
        self._table.setHorizontalHeaderLabels(["Job", "Mode", "Status", "Progress"])
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self._table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for row, job in enumerate(self._jobs.values()):
            self._row_index[job.name] = row
            self._table.setItem(row, 0, QtWidgets.QTableWidgetItem(job.name))
            self._table.setItem(row, 1, QtWidgets.QTableWidgetItem(job.mode))
            self._table.setItem(row, 2, QtWidgets.QTableWidgetItem(job.status))
            bar = QtWidgets.QProgressBar(self)
            bar.setValue(job.progress)
            self._table.setCellWidget(row, 3, bar)

        layout.addWidget(self._table)

        controls = QtWidgets.QHBoxLayout()
        self._start_button = QtWidgets.QPushButton("Run Selected Job", self)
        self._start_button.clicked.connect(self._run_selected)
        controls.addWidget(self._start_button)
        controls.addStretch(1)
        layout.addLayout(controls)

        self._status = QtWidgets.QLabel("Idle")
        layout.addWidget(self._status)

    def _run_selected(self) -> None:
        row = self._table.currentRow()
        if row < 0:
            self._status.setText("Select a job to execute")
            return
        job_name = self._table.item(row, 0).text()
        job = self._jobs[job_name]
        runner = JobRunner(job)
        runner.signals.progress.connect(self._on_progress)
        runner.signals.finished.connect(self._on_finished)
        self._status.setText(f"Running {job.name} on {job.mode}")
        self._thread_pool.start(runner)

    @QtCore.Slot(str, int)
    def _on_progress(self, name: str, value: int) -> None:
        job = self._jobs[name]
        job.progress = value
        row = self._row_index[name]
        bar = self._table.cellWidget(row, 3)
        if isinstance(bar, QtWidgets.QProgressBar):
            bar.setValue(value)
        status_item = self._table.item(row, 2)
        if status_item:
            status_item.setText("running")

    @QtCore.Slot(str)
    def _on_finished(self, name: str) -> None:
        job = self._jobs[name]
        job.status = "complete"
        row = self._row_index[name]
        status_item = self._table.item(row, 2)
        if status_item:
            status_item.setText(job.status)
        self._status.setText(f"{name} complete")


__all__ = ["AsyncJobsPanel"]
