"""Pipeline actions."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtCore, QtWidgets


class PipelinePanel(QtWidgets.QGroupBox):
    """Trigger and monitor pipelines."""

    pipelineTriggered = QtCore.Signal(str)

    def __init__(self, pipelines: Iterable[str]) -> None:
        super().__init__("Pipelines")
        self._pipelines = list(pipelines)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(self._pipelines)

        trigger_button = QtWidgets.QPushButton("Trigger")
        trigger_button.clicked.connect(self._emit_trigger)

        layout.addWidget(self.combo)
        layout.addWidget(trigger_button)

        self.log_view = QtWidgets.QTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setPlaceholderText("Pipeline logs appear here...")
        layout.addWidget(self.log_view)

    def _emit_trigger(self) -> None:
        pipeline = self.combo.currentText()
        self.pipelineTriggered.emit(pipeline)
        self.log_view.append(f"<span style='color:#8A0303;'>▶</span> Triggered {pipeline}")


__all__ = ["PipelinePanel"]
