"""Panel for AI training lifecycle."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import AITrainingRun


class AITrainingPanel(QtWidgets.QWidget):
    """Surface state of custom training and evaluation runs."""

    def __init__(self, runs: Iterable[AITrainingRun]):
        super().__init__()
        self._runs = list(runs)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Monitor reinforcement learning cycles, dataset refreshes, and evaluation "
            "scores across the AI platform."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Run", "Dataset", "Status", "Metric"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)
        tree.setUniformRowHeights(True)
        tree.header().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        for run in self._runs:
            item = QtWidgets.QTreeWidgetItem([run.name, run.dataset, run.status, run.metric])
            tree.addTopLevelItem(item)

        layout.addWidget(tree)

        footer = QtWidgets.QLabel(
            "Schedule nightly fine-tunes with the cron panel or trigger ad-hoc "
            "training bursts through automation scripts that call the AI service."
        )
        footer.setWordWrap(True)
        footer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        footer.setStyleSheet("color: #C0C0C0;")
        layout.addWidget(footer)


__all__ = ["AITrainingPanel"]
