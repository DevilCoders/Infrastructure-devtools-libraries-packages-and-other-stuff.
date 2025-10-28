"""Security policy insights panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets

from ...core.state import SecurityPolicy


class SecurityPanel(QtWidgets.QWidget):
    """Expose security policies and compliance drift."""

    def __init__(self, policies: Iterable[SecurityPolicy]):
        super().__init__()
        self._policies = list(policies)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        blurb = QtWidgets.QLabel(
            "Track compliance, rotation cadence, and audit currency in one snapshot."
        )
        blurb.setWordWrap(True)
        layout.addWidget(blurb)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Policy", "Coverage", "Status", "Last Audit"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for policy in self._policies:
            item = QtWidgets.QTreeWidgetItem(
                [policy.name, policy.coverage, policy.status, policy.last_audit]
            )
            tree.addTopLevelItem(item)

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["SecurityPanel"]
