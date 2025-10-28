"""Tenant overview panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets

from ...core.state import TenantProfile


class TenantPanel(QtWidgets.QWidget):
    """Summaries of tenant environments."""

    def __init__(self, tenants: Iterable[TenantProfile]):
        super().__init__()
        self._tenants = list(tenants)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        tree = QtWidgets.QTreeWidget(self)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Tenant", "Environments", "Owner", "Health"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)

        for tenant in self._tenants:
            environments = ", ".join(tenant.environments)
            tree.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [tenant.name, environments, tenant.owner, tenant.health]
                )
            )

        tree.header().setStretchLastSection(True)
        layout.addWidget(tree)


__all__ = ["TenantPanel"]
