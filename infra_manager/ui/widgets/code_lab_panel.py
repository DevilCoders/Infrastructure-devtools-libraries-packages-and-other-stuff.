"""Panel exposing code authoring and execution workflows."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtCore, QtWidgets

from ...core.state import CodeWorkspace


class CodeLabPanel(QtWidgets.QWidget):
    """Allow operators to draft automation code and simulate runs inline."""

    def __init__(self, workspaces: Iterable[CodeWorkspace]):
        super().__init__()
        self._workspaces = list(workspaces)
        self._build_ui()

    # ------------------------------------------------------------------
    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        banner = QtWidgets.QLabel(
            "Draft infrastructure automations in Python, Bash, or Batch and replay them "
            "through simulated runners before shipping to production."
        )
        banner.setWordWrap(True)
        layout.addWidget(banner)

        selector_row = QtWidgets.QHBoxLayout()
        selector_row.setSpacing(8)

        selector_label = QtWidgets.QLabel("Workspace:")
        selector_row.addWidget(selector_label)

        self._workspace_combo = QtWidgets.QComboBox(self)
        for workspace in self._workspaces:
            self._workspace_combo.addItem(workspace.name, workspace)
        self._workspace_combo.currentIndexChanged.connect(self._on_workspace_changed)
        selector_row.addWidget(self._workspace_combo, 1)

        self._runner_label = QtWidgets.QLabel("")
        self._runner_label.setStyleSheet("color: #C0C0C0;")
        selector_row.addWidget(self._runner_label)

        layout.addLayout(selector_row)

        self._description = QtWidgets.QTextBrowser(self)
        self._description.setMaximumHeight(120)
        self._description.setOpenExternalLinks(True)
        layout.addWidget(self._description)

        self._editor = QtWidgets.QPlainTextEdit(self)
        self._editor.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self._editor.setTabStopDistance(4 * self.fontMetrics().horizontalAdvance(" "))
        layout.addWidget(self._editor, 1)

        controls = QtWidgets.QHBoxLayout()
        controls.addStretch(1)
        run_button = QtWidgets.QPushButton("Run Workspace", self)
        run_button.clicked.connect(self._run_workspace)
        controls.addWidget(run_button)
        layout.addLayout(controls)

        self._console = QtWidgets.QTextEdit(self)
        self._console.setReadOnly(True)
        self._console.setMinimumHeight(160)
        self._console.setStyleSheet("background-color: rgba(20,20,20,0.8);")
        layout.addWidget(self._console)

        if self._workspaces:
            self._workspace_combo.setCurrentIndex(0)
            self._on_workspace_changed(0)

    # ------------------------------------------------------------------
    def _on_workspace_changed(self, index: int) -> None:
        workspace: CodeWorkspace = self._workspace_combo.itemData(index)
        if workspace is None:
            self._editor.clear()
            self._description.clear()
            self._runner_label.clear()
            return
        self._editor.setPlainText(workspace.template)
        self._description.setHtml(
            f"""
            <h3 style='color:#FF3355;'>{workspace.name}</h3>
            <p>Language: <b>{workspace.language}</b></p>
            <p>{workspace.description}</p>
            """
        )
        self._runner_label.setText(f"Runner: {workspace.runner}")
        self._console.append(
            f"[workspace] Loaded {workspace.name} using {workspace.language} template."
        )

    # ------------------------------------------------------------------
    def _run_workspace(self) -> None:
        index = self._workspace_combo.currentIndex()
        workspace: CodeWorkspace = self._workspace_combo.itemData(index)
        if workspace is None:
            return
        code = self._editor.toPlainText().strip()
        preview = code.splitlines()[0] if code else "(empty script)"
        self._console.append(
            f"[run] Dispatching '{workspace.name}' via {workspace.runner}\n"
            f"      Language: {workspace.language}\n"
            f"      Preview: {preview}"
        )
        self._console.ensureCursorVisible()


# Avoid circular import at runtime.
from PySide6 import QtGui  # noqa: E402  (import after QtWidgets usage)


__all__ = ["CodeLabPanel"]
