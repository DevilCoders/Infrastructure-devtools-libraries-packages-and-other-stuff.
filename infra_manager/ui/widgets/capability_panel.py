"""Panel describing a dynamically generated command center tab."""
from __future__ import annotations

from PySide6 import QtWidgets

from ...core.state import CommandCenterTab


class CapabilityPanel(QtWidgets.QWidget):
    """Display focus, highlights, and automations for a capability."""

    def __init__(self, descriptor: CommandCenterTab) -> None:
        super().__init__()
        self._descriptor = descriptor
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        title = QtWidgets.QLabel(self._descriptor.title)
        title.setStyleSheet("font-size: 20px; font-weight: 600;")
        layout.addWidget(title)

        focus = QtWidgets.QLabel(f"Focus: <b>{self._descriptor.focus}</b>")
        focus.setWordWrap(True)
        layout.addWidget(focus)

        description = QtWidgets.QLabel(self._descriptor.description)
        description.setWordWrap(True)
        layout.addWidget(description)

        if self._descriptor.highlights:
            highlights_group = QtWidgets.QGroupBox("Highlights")
            highlights_layout = QtWidgets.QVBoxLayout(highlights_group)
            for item in self._descriptor.highlights:
                label = QtWidgets.QLabel(f"• {item}")
                label.setWordWrap(True)
                highlights_layout.addWidget(label)
            layout.addWidget(highlights_group)

        if self._descriptor.automations:
            automation_group = QtWidgets.QGroupBox("Automation Hooks")
            automation_layout = QtWidgets.QVBoxLayout(automation_group)
            for item in self._descriptor.automations:
                label = QtWidgets.QLabel(f"→ {item}")
                label.setWordWrap(True)
                automation_layout.addWidget(label)
            layout.addWidget(automation_group)

        layout.addStretch(1)


__all__ = ["CapabilityPanel"]
