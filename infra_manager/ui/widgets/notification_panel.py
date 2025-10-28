"""Notification and ChatOps panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import NotificationChannel


class NotificationPanel(QtWidgets.QWidget):
    """Display notification channels and routing targets."""

    def __init__(self, channels: Iterable[NotificationChannel]):
        super().__init__()
        self._channels = list(channels)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        note = QtWidgets.QLabel("Wire PagerDuty, Slack, and email feeds with one click.")
        layout.addWidget(note)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Channel", "Medium", "Target", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for channel in self._channels:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [channel.name, channel.medium, channel.target, channel.status]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["NotificationPanel"]
