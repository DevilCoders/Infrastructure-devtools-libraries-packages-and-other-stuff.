"""Automation script palette panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import AutomationScript


class AutomationPanel(QtWidgets.QWidget):
    """Showcase multi-language automation scripts."""

    def __init__(self, scripts: Iterable[AutomationScript]):
        super().__init__()
        self._scripts = list(scripts)
        self._build_ui()

    def _build_ui(self) -> None:
        splitter = QtWidgets.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)

        tree = QtWidgets.QTreeWidget(splitter)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Script", "Language", "Target", "Summary"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)
        tree.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        tree.setUniformRowHeights(True)

        for script in self._scripts:
            item = QtWidgets.QTreeWidgetItem(
                [script.name, script.language, script.target, script.summary]
            )
            tree.addTopLevelItem(item)

        editor = QtWidgets.QPlainTextEdit(splitter)
        editor.setReadOnly(True)
        editor.setPlaceholderText("Select an automation to view its snippet")

        tree.currentItemChanged.connect(
            lambda current, _: editor.setPlainText(
                next(
                    (s.snippet for s in self._scripts if s.name == current.text(0)),
                    "",
                )
                if current
                else ""
            )
        )

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Run automation in Python, Bash, or Batch with a unified trigger surface."
        )
        header.setWordWrap(True)
        layout.addWidget(header)
        layout.addWidget(splitter)


__all__ = ["AutomationPanel"]
