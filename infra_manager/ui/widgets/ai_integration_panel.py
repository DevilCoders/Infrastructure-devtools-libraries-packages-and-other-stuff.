"""Panel for AI powered integrations."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import AIIntegration


class AIIntegrationPanel(QtWidgets.QWidget):
    """Detail how AI services connect with automation endpoints."""

    def __init__(self, integrations: Iterable[AIIntegration]):
        super().__init__()
        self._integrations = list(integrations)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Wire the homegrown AI orchestrator into chat platforms, Git providers, "
            "and CI engines for closed-loop automation."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Integration", "Interface", "Capability", "Endpoint"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)
        tree.setUniformRowHeights(True)
        tree.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        for integration in self._integrations:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [
                        integration.name,
                        integration.interface,
                        integration.capability,
                        integration.endpoint,
                    ]
                )
            )

        layout.addWidget(tree)

        footer = QtWidgets.QLabel(
            "Use the automation panel to push new integration manifests or roll the "
            "AI gateway without downtime."
        )
        footer.setWordWrap(True)
        footer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        footer.setStyleSheet("color: #C0C0C0;")
        layout.addWidget(footer)


__all__ = ["AIIntegrationPanel"]
