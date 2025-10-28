"""Cron scheduler management panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtWidgets

from ...core.state import CronSchedule


class SchedulerPanel(QtWidgets.QWidget):
    """Expose cron schedule inventory."""

    def __init__(self, schedules: Iterable[CronSchedule]):
        super().__init__()
        self._schedules = list(schedules)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        caption = QtWidgets.QLabel(
            "Observe and toggle fleet-wide cron entries with drift control."
        )
        caption.setWordWrap(True)
        layout.addWidget(caption)

        table = QtWidgets.QTableWidget(len(self._schedules), 4, self)
        table.setHorizontalHeaderLabels(["Schedule", "Expression", "Command", "Enabled"])
        table.horizontalHeader().setStretchLastSection(True)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for row, schedule in enumerate(self._schedules):
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(schedule.name))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(schedule.schedule))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(schedule.command))
            checkbox = QtWidgets.QCheckBox(self)
            checkbox.setChecked(schedule.enabled)
            checkbox.stateChanged.connect(
                lambda state, sched=schedule: self._on_toggle(sched, bool(state))
            )
            table.setCellWidget(row, 3, checkbox)

        layout.addWidget(table)

        self._status = QtWidgets.QLabel("Select a schedule to toggle enablement")
        layout.addWidget(self._status)

    def _on_toggle(self, schedule: CronSchedule, enabled: bool) -> None:
        schedule.enabled = enabled
        self._status.setText(
            f"{schedule.name}: {'enabled' if enabled else 'disabled'}"
        )


__all__ = ["SchedulerPanel"]
