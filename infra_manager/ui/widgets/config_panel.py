"""Advanced configuration templates panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import ConfigurationTemplate


class ConfigurationPanel(QtWidgets.QGroupBox):
    """Browse and edit advanced configuration templates."""

    templateSelected = QtCore.Signal(ConfigurationTemplate)

    def __init__(self, templates: Iterable[ConfigurationTemplate]) -> None:
        super().__init__("Advanced Configurations")
        self._templates = list(templates)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QHBoxLayout(self)

        self.list_widget = QtWidgets.QListWidget(self)
        for template in self._templates:
            item = QtWidgets.QListWidgetItem(f"{template.name} · {template.scope}")
            item.setData(QtCore.Qt.ItemDataRole.UserRole, template)
            self.list_widget.addItem(item)
        layout.addWidget(self.list_widget)

        self.editor = QtWidgets.QTextEdit(self)
        self.editor.setPlaceholderText("Select a template to view configuration blueprint and patch guidance.")
        layout.addWidget(self.editor)

        self.list_widget.currentItemChanged.connect(self._update_editor)

    # ------------------------------------------------------------------
    def _update_editor(self, current: QtWidgets.QListWidgetItem | None) -> None:
        if not current:
            self.editor.clear()
            return
        template = current.data(QtCore.Qt.ItemDataRole.UserRole)
        if not template:
            self.editor.clear()
            return
        self.editor.setPlainText(
            f"Template: {template.name}\n"
            f"Scope: {template.scope}\n"
            f"Version: {template.version}\n\n"
            f"{template.description}\n"
            "---\n# Apply overrides below\n"
        )
        self.templateSelected.emit(template)


__all__ = ["ConfigurationPanel"]
