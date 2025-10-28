"""Local deployment tooling panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal

from ...core.state import DeploymentProfile


class DeploymentPanel(QtWidgets.QGroupBox):
    """Coordinate local deployment orchestration."""

    deploymentRequested = pyqtSignal(DeploymentProfile)

    def __init__(self, profiles: Iterable[DeploymentProfile]) -> None:
        super().__init__("Local Deployment")
        self._profiles = list(profiles)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        self.combo = QtWidgets.QComboBox(self)
        for profile in self._profiles:
            self.combo.addItem(profile.name, profile)
        layout.addWidget(self.combo)

        self.details = QtWidgets.QTextBrowser(self)
        self.details.setPlaceholderText("Select a profile to view rollout notes, manifests, and overrides.")
        layout.addWidget(self.details)

        trigger = QtWidgets.QPushButton("Launch")
        trigger.clicked.connect(self._emit_deploy)
        layout.addWidget(trigger)

        self.combo.currentIndexChanged.connect(self._update_details)
        self._update_details(0)

    # ------------------------------------------------------------------
    def _update_details(self, _: int) -> None:
        profile = self.combo.currentData()
        if not profile:
            self.details.clear()
            return
        self.details.setHtml(
            f"""
            <h3 style='color:#FF0040;'>{profile.name}</h3>
            <p><b>Target:</b> {profile.target}</p>
            <p><b>Strategy:</b> {profile.strategy}</p>
            <p><b>Last Run:</b> {profile.last_run}</p>
            """
        )

    def _emit_deploy(self) -> None:
        profile = self.combo.currentData()
        if profile:
            self.deploymentRequested.emit(profile)


__all__ = ["DeploymentPanel"]
