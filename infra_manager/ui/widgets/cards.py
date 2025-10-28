"""Reusable card widgets."""
from __future__ import annotations

from PyQt6 import QtCore, QtGui, QtWidgets


class MetricCard(QtWidgets.QFrame):
    """Simple frosted glass style metric card."""

    def __init__(self, title: str, value: int | str) -> None:
        super().__init__()
        self.setObjectName("metricCard")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setFixedHeight(120)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)

        title_label = QtWidgets.QLabel(title.upper())
        title_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        title_label.setStyleSheet("font-size: 12px; letter-spacing: 2px; color: rgba(255,255,255,0.6);")

        value_label = QtWidgets.QLabel(str(value))
        value_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        value_label.setStyleSheet("font-size: 34px; font-weight: 600;")

        layout.addWidget(title_label)
        layout.addStretch(1)
        layout.addWidget(value_label)

        self._pulse_animation()

    def _pulse_animation(self) -> None:
        effect = QtWidgets.QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(24)
        effect.setOffset(0, 0)
        effect.setColor(QtGui.QColor(QtCore.Qt.GlobalColor.red))
        self.setGraphicsEffect(effect)

        animation = QtCore.QPropertyAnimation(effect, b"blurRadius", self)
        animation.setDuration(1600)
        animation.setStartValue(24)
        animation.setEndValue(8)
        animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        animation.setLoopCount(-1)
        animation.start(
            QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped
        )


__all__ = ["MetricCard"]
