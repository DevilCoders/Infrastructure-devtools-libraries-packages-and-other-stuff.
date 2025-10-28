"""Panel for AI assistant overviews."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import AIAssistant


class AIAssistantPanel(QtWidgets.QWidget):
    """Display the available custom AI copilots."""

    ASSISTANT_ROLE = QtCore.Qt.ItemDataRole.UserRole

    def __init__(self, assistants: Iterable[AIAssistant]):
        super().__init__()
        self._assistants = list(assistants)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Summon bespoke AI copilots that understand your infrastructure estate, "
            "governance model, and deployment rituals."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        splitter = QtWidgets.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)

        roster = QtWidgets.QListWidget(splitter)
        roster.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        roster.setAlternatingRowColors(True)

        detail = QtWidgets.QTextBrowser(splitter)
        detail.setOpenExternalLinks(True)
        detail.setPlaceholderText("Select an assistant to inspect capabilities")

        for assistant in self._assistants:
            item = QtWidgets.QListWidgetItem(
                f"{assistant.name} — {assistant.specialization.title()}"
            )
            item.setData(self.ASSISTANT_ROLE, assistant)
            roster.addItem(item)

        roster.currentItemChanged.connect(self._on_roster_selection_changed)
        self._detail = detail

        if roster.count():
            roster.setCurrentRow(0)

        layout.addWidget(splitter)

    def _render_assistant(self, item: QtWidgets.QListWidgetItem | None) -> str:
        assistant = item.data(self.ASSISTANT_ROLE) if item else None
        if not assistant:
            return ""
        return (
            f"<h3 style='color:#FF0040;'>{assistant.name}</h3>"
            f"<p><b>Specialization:</b> {assistant.specialization}</p>"
            f"<p><b>Availability:</b> {assistant.availability}</p>"
            f"<p>{assistant.description}</p>"
            "<p>Trigger assistants via chat, slash commands, or automation hooks "
            "and they will coordinate with the AI orchestration service.</p>"
        )

    def _on_roster_selection_changed(
        self, current: QtWidgets.QListWidgetItem | None, _: QtWidgets.QListWidgetItem | None
    ) -> None:
        """Render assistant details when the selection changes."""
        if not hasattr(self, "_detail"):
            return
        self._detail.setHtml(self._render_assistant(current))


__all__ = ["AIAssistantPanel"]
