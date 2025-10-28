"""Cluster management panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import Cluster


class ClusterPanel(QtWidgets.QGroupBox):
    """Display active clusters and capacity data."""

    def __init__(self, clusters: Iterable[Cluster]) -> None:
        super().__init__("Clusters")
        self._clusters = list(clusters)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setHeaderLabels(["Cluster", "Provider", "Nodes", "Version", "Status", "Region"])
        self.tree.header().setStretchLastSection(True)

        for cluster in self._clusters:
            item = QtWidgets.QTreeWidgetItem(
                [
                    cluster.name,
                    cluster.provider,
                    str(cluster.nodes),
                    cluster.version,
                    cluster.status,
                    cluster.region,
                ]
            )
            self.tree.addTopLevelItem(item)

        layout.addWidget(self.tree)

        self.actions = QtWidgets.QHBoxLayout()
        scale_button = QtWidgets.QPushButton("Scale")
        diagnose_button = QtWidgets.QPushButton("Diagnose")
        self.actions.addWidget(scale_button)
        self.actions.addWidget(diagnose_button)
        self.actions.addStretch(1)
        layout.addLayout(self.actions)


__all__ = ["ClusterPanel"]
