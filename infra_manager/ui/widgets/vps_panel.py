"""Virtual private servers panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal

from ...core.state import VirtualServer


class VPSPanel(QtWidgets.QGroupBox):
    """Manage VPS resources and lifecycle."""

    serverActionRequested = pyqtSignal(str, str)

    def __init__(self, servers: Iterable[VirtualServer]) -> None:
        super().__init__("VPS Fleet")
        self._servers = list(servers)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(len(self._servers), 5, self)
        self.table.setHorizontalHeaderLabels(["Name", "Provider", "CPU", "Memory", "Status"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for row, server in enumerate(self._servers):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(server.name))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(server.provider))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(server.cpu))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(server.memory))
            status = QtWidgets.QTableWidgetItem(server.status.title())
            status.setData(Qt.ItemDataRole.UserRole, server.location)
            self.table.setItem(row, 4, status)

        layout.addWidget(self.table)

        controls = QtWidgets.QHBoxLayout()
        reboot_button = QtWidgets.QPushButton("Reboot")
        reboot_button.clicked.connect(lambda: self._emit_action("reboot"))
        snapshot_button = QtWidgets.QPushButton("Snapshot")
        snapshot_button.clicked.connect(lambda: self._emit_action("snapshot"))
        controls.addWidget(reboot_button)
        controls.addWidget(snapshot_button)
        controls.addStretch(1)

        layout.addLayout(controls)

    # ------------------------------------------------------------------
    def _emit_action(self, action: str) -> None:
        row = self.table.currentRow()
        if row < 0:
            return
        name_item = self.table.item(row, 0)
        location_item = self.table.item(row, 4)
        if not name_item or not location_item:
            return
        location = location_item.data(Qt.ItemDataRole.UserRole) or ""
        self.serverActionRequested.emit(action, f"{name_item.text()}@{location}")


__all__ = ["VPSPanel"]
