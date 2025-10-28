"""Infrastructure blueprint gallery panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import Blueprint


class BlueprintPanel(QtWidgets.QWidget):
    """Display curated infrastructure blueprints."""

    def __init__(self, blueprints: Iterable[Blueprint]):
        super().__init__()
        self._blueprints = list(blueprints)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(3)
        tree.setHeaderLabels(["Blueprint", "Scope", "Maturity"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for blueprint in self._blueprints:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [blueprint.name, blueprint.scope, blueprint.maturity]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["BlueprintPanel"]
