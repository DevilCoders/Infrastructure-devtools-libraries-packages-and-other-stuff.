"""FinOps cost strategy panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets

from ...core.state import CostStrategy


class CostPanel(QtWidgets.QWidget):
    """Highlight savings initiatives."""

    def __init__(self, strategies: Iterable[CostStrategy]):
        super().__init__()
        self._strategies = list(strategies)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(3)
        tree.setHeaderLabels(["Strategy", "Focus", "Savings"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for strategy in self._strategies:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [strategy.name, strategy.focus, strategy.savings]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["CostPanel"]
