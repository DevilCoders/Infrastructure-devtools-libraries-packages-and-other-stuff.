"""Observability probes panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets

from ...core.state import ObservabilityProbe


class ObservabilityPanel(QtWidgets.QWidget):
    """Render observability probes and their status."""

    def __init__(self, probes: Iterable[ObservabilityProbe]):
        super().__init__()
        self._probes = list(probes)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        info = QtWidgets.QLabel(
            "Fine-tune service level signals across clusters and toolchains."
        )
        layout.addWidget(info)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Probe", "Kind", "Target", "Status"])
        tree.setRootIsDecorated(False)
        tree.setUniformRowHeights(True)
        tree.setAlternatingRowColors(True)

        for probe in self._probes:
            item = QtWidgets.QTreeWidgetItem([probe.name, probe.kind, probe.target, probe.status])
            tree.addTopLevelItem(item)

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["ObservabilityPanel"]
