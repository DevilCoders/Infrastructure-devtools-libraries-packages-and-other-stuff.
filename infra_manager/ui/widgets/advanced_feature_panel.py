"""Panel presenting advanced feature catalog."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets

from ...core.state import AdvancedFeature


class AdvancedFeaturePanel(QtWidgets.QWidget):
    """Display a matrix of advanced capabilities bundled with the studio."""

    def __init__(self, features: Iterable[AdvancedFeature]):
        super().__init__()
        self._features = list(features)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QtWidgets.QLabel(
            "Explore more than thirty advanced operator-centric capabilities,\n"
            "from concurrency orchestration to governance guardrails."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Feature", "Category", "Description", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)
        tree.setUniformRowHeights(True)

        for feature in self._features:
            item = QtWidgets.QTreeWidgetItem(
                [feature.name, feature.category, feature.description, feature.status]
            )
            tree.addTopLevelItem(item)

        tree.header().setStretchLastSection(True)
        tree.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        tree.header().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        layout.addWidget(tree)


__all__ = ["AdvancedFeaturePanel"]
