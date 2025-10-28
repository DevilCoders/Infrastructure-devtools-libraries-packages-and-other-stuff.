"""Service mesh policy panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import ServiceMeshPolicy


class ServiceMeshPanel(QtWidgets.QWidget):
    """Surface service mesh policy state."""

    def __init__(self, policies: Iterable[ServiceMeshPolicy]):
        super().__init__()
        self._policies = list(policies)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Policy", "Mesh", "Mode", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for policy in self._policies:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [policy.name, policy.mesh, policy.mode, policy.status]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["ServiceMeshPanel"]
