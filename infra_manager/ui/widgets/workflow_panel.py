"""Workflow management panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets


class WorkflowPanel(QtWidgets.QGroupBox):
    """Display and request workflow runs."""

    workflowRequested = QtCore.pyqtSignal(str)

    def __init__(self, workflows: Iterable[str]) -> None:
        super().__init__("Workflows")
        self._workflows = list(workflows)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        self.list_widget = QtWidgets.QListWidget()
        for workflow in self._workflows:
            item = QtWidgets.QListWidgetItem(workflow)
            self.list_widget.addItem(item)
        layout.addWidget(self.list_widget)

        run_button = QtWidgets.QPushButton("Request Run")
        run_button.clicked.connect(self._request_run)
        layout.addWidget(run_button)

        self.notes = QtWidgets.QTextEdit()
        self.notes.setPlaceholderText("Describe the desired workflow customization...")
        layout.addWidget(self.notes)

    def _request_run(self) -> None:
        item = self.list_widget.currentItem()
        if not item:
            QtWidgets.QMessageBox.warning(self, "Workflow", "Select a workflow to request a run")
            return
        workflow = item.text()
        notes = self.notes.toPlainText().strip()
        payload = f"{workflow} — Notes: {notes or 'none'}"
        self.workflowRequested.emit(payload)


__all__ = ["WorkflowPanel"]
