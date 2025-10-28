"""Reusable card widgets."""
from __future__ import annotations

from PyQt6 import QtCore, QtGui, QtWidgets


class MetricCard(QtWidgets.QFrame):
    """Simple frosted glass style metric card."""

    def __init__(self, title: str, value: int | str) -> None:
        super().__init__()
        self.setObjectName("metricCard")
        self.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.setFixedHeight(140)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)

        title_label = QtWidgets.QLabel(title.upper())
        title_label.setObjectName("metricTitle")
        title_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter
        )

        value_label = QtWidgets.QLabel(str(value))
        value_label.setObjectName("metricValue")
        value_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(title_label)
        layout.addStretch(1)
        layout.addWidget(value_label)

        self._pulse_animation()

    def _pulse_animation(self) -> None:
        effect = QtWidgets.QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(28)
        effect.setOffset(0, 0)
        effect.setColor(QtGui.QColor(255, 0, 120, 120))
        self.setGraphicsEffect(effect)

        animation = QtCore.QPropertyAnimation(effect, b"blurRadius", self)
        animation.setDuration(2200)
        animation.setStartValue(30)
        animation.setEndValue(12)
        animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuad)
        animation.setLoopCount(-1)
        animation.start(QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)


__all__ = ["MetricCard"]
