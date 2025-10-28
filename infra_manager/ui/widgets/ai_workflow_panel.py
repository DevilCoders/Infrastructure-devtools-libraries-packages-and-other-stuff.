"""Panel for AI workflow orchestration."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import AIWorkflow


class AIWorkflowPanel(QtWidgets.QWidget):
    """Expose programmable AI workflows and their guardrails."""

    def __init__(self, workflows: Iterable[AIWorkflow]):
        super().__init__()
        self._workflows = list(workflows)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Author bespoke AI workflows, align them to infrastructure objectives, "
            "and surface guardrails before execution."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Workflow", "Entrypoint", "Objective", "Guardrails"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)
        tree.setUniformRowHeights(True)
        tree.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        for workflow in self._workflows:
            item = QtWidgets.QTreeWidgetItem(
                [
                    workflow.name,
                    workflow.entrypoint,
                    workflow.objective,
                    workflow.guardrails,
                ]
            )
            tree.addTopLevelItem(item)

        layout.addWidget(tree)

        hint = QtWidgets.QLabel(
            "Tip: workflows can dispatch into async jobs, cron schedules, or bulk "
            "operations for deterministic execution after AI planning."
        )
        hint.setWordWrap(True)
        hint.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
        )
        hint.setStyleSheet("color: #C0C0C0;")
        layout.addWidget(hint)


__all__ = ["AIWorkflowPanel"]
