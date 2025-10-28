"""Data pipeline observability panel."""
from __future__ import annotations

from typing import Iterable

from PySide6 import QtWidgets

from ...core.state import DataPipeline


class DataPipelinePanel(QtWidgets.QWidget):
    """Show data pipeline health."""

    def __init__(self, pipelines: Iterable[DataPipeline]):
        super().__init__()
        self._pipelines = list(pipelines)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Pipeline", "Schedule", "Owner", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for pipeline in self._pipelines:
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [pipeline.name, pipeline.schedule, pipeline.owner, pipeline.status]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["DataPipelinePanel"]
