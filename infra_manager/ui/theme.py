"""Theme helpers used across the UI."""
from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path
from string import Template
from typing import Optional

from PyQt6 import QtCore, QtGui

from . import resources

try:
    from PyQt6 import QtWidgets
except ImportError:  # pragma: no cover - handled by runtime environment
    QtWidgets = None  # type: ignore


@dataclass(frozen=True)
class Theme:
    """Centralized styling for the application."""

    background_color: str
    accent_color: str
    accent_secondary: str
    text_color: str
    muted_text_color: str
    card_color: str
    border_radius: int = 14
    background_image: Optional[Path] = None

    @classmethod
    def default(cls) -> "Theme":
        return cls(
            background_color="#050312",
            accent_color="#FF0040",
            accent_secondary="#6200EA",
            text_color="#F5F5F7",
            muted_text_color="rgba(255,255,255,0.55)",
            card_color="#121425",
        )

    @staticmethod
    @lru_cache(maxsize=1)
    def _stylesheet_template() -> Template:
        return Template(resources.NEON_STYLESHEET)

    def stylesheet(self) -> str:
        """Return the global Qt stylesheet."""

        bg_image = (
            "background-image: url('" + self.background_image.as_posix() + "');"
            "background-position: center; background-attachment: fixed;"
            "background-repeat: no-repeat;"
            if self.background_image
            else ""
        )
        return self._stylesheet_template().safe_substitute(
            background=self.background_color,
            text=self.text_color,
            mutedText=self.muted_text_color,
            accent=self.accent_color,
            accentSecondary=self.accent_secondary,
            card=self.card_color,
            borderRadius=str(self.border_radius),
            backgroundImage=bg_image,
        )

    def palette(self) -> QtGui.QPalette:
        palette = QtGui.QPalette()
        background = QtGui.QColor(self.background_color)
        card = QtGui.QColor(self.card_color)
        text = QtGui.QColor(self.text_color)

        palette.setColor(QtGui.QPalette.ColorRole.Window, background)
        palette.setColor(QtGui.QPalette.ColorRole.WindowText, text)
        palette.setColor(QtGui.QPalette.ColorRole.Base, card)
        palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, card)
        palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, card)
        palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, text)
        palette.setColor(QtGui.QPalette.ColorRole.Text, text)
        palette.setColor(QtGui.QPalette.ColorRole.Button, card)
        palette.setColor(QtGui.QPalette.ColorRole.ButtonText, text)
        palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(self.accent_color))
        palette.setColor(QtGui.QPalette.ColorRole.HighlightedText, QtGui.QColor("white"))
        return palette

    def font(self) -> QtGui.QFont:
        font = QtGui.QFont("Segoe UI")
        font.setPointSize(10)
        font.setHintingPreference(QtGui.QFont.HintingPreference.PreferFullHinting)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        return font

    def apply(self, widget: QtCore.QObject) -> None:
        """Apply the theme to a widget tree."""

        if isinstance(widget, QtWidgets.QApplication):  # type: ignore[attr-defined]
            widget.setPalette(self.palette())
            widget.setStyleSheet(self.stylesheet())
            widget.setFont(self.font())
        elif isinstance(widget, QtWidgets.QWidget):  # type: ignore[attr-defined]
            widget.setPalette(self.palette())
            widget.setStyleSheet(self.stylesheet())
            widget.setFont(self.font())

    def with_background(self, path: Path) -> "Theme":
        return replace(self, background_image=path)


__all__ = ["Theme"]
