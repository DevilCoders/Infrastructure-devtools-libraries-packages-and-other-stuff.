"""Central logging sink panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import LoggingSink


class LoggingPanel(QtWidgets.QWidget):
    """Surface logging sink configuration."""

    def __init__(self, sinks: Iterable[LoggingSink]):
        super().__init__()
        self._sinks = list(sinks)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Sink", "Destination", "Retention", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for sink in self._sinks:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [sink.name, sink.destination, sink.retention, sink.status]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["LoggingPanel"]
