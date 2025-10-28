"""Theme helpers used across the UI."""
from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Optional

from PySide6 import QtCore, QtGui


@dataclass(frozen=True)
class Theme:
    """Centralized styling for the application."""

    background_color: str
    accent_color: str
    text_color: str
    card_color: str
    border_radius: int = 12
    background_image: Optional[Path] = None

    @classmethod
    def default(cls) -> "Theme":
        return cls(
            background_color="#111111",
            accent_color="#8A0303",
            text_color="#E4E4E4",
            card_color="#1F1F1F",
        )

    def stylesheet(self) -> str:
        """Return the global Qt stylesheet."""

        bg_image = (
            f"background-image: url('{self.background_image.as_posix()}');"
            "background-position: center; background-repeat: no-repeat;"
            if self.background_image
            else ""
        )
        return f"""
            QWidget {{
                background-color: {self.background_color};
                color: {self.text_color};
                {bg_image}
            }}
            QToolBar {{
                background-color: rgba(30, 30, 30, 200);
                border: none;
            }}
            QStatusBar {{
                background-color: rgba(20, 20, 20, 180);
                border-top: 1px solid {self.accent_color};
            }}
            QPushButton {{
                background-color: {self.accent_color};
                color: {self.text_color};
                border-radius: {self.border_radius}px;
                padding: 6px 14px;
            }}
            QPushButton:hover {{
                background-color: rgba(138, 3, 3, 0.8);
            }}
            QLineEdit, QTextEdit, QListWidget {{
                background-color: {self.card_color};
                border-radius: {self.border_radius}px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                padding: 6px;
            }}
            QTabWidget::pane {{
                border: 1px solid rgba(255, 255, 255, 0.04);
                border-radius: {self.border_radius}px;
                padding: 6px;
                background-color: {self.background_color};
            }}
            QTabBar::tab {{
                background-color: {self.card_color};
                color: {self.text_color};
                padding: 10px 18px;
                margin: 0 4px;
                border-top-left-radius: {self.border_radius}px;
                border-top-right-radius: {self.border_radius}px;
            }}
            QTabBar::tab:selected {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(255, 0, 64, 0.9),
                    stop:1 rgba(138, 3, 3, 0.9));
                color: white;
            }}
            QTabBar::tab:hover {{
                background-color: rgba(138, 3, 3, 0.6);
            }}
            QTreeWidget, QTableWidget {{
                background-color: {self.card_color};
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: {self.border_radius}px;
            }}
            QSplitter::handle {{
                background-color: rgba(255, 0, 64, 0.1);
            }}
            QTextBrowser {{
                background-color: rgba(17, 17, 17, 0.6);
                border: 1px solid rgba(255, 0, 64, 0.15);
                border-radius: {self.border_radius}px;
            }}
        """

    def palette(self) -> QtGui.QPalette:
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(self.background_color))
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(self.text_color))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(self.card_color))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(self.card_color))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(self.card_color))
        palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(self.text_color))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(self.text_color))
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(self.card_color))
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(self.text_color))
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(self.accent_color))
        palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor("white"))
        return palette

    def apply(self, widget: QtCore.QObject) -> None:
        """Apply the theme to a widget tree."""

        if isinstance(widget, QtWidgets.QApplication):  # type: ignore[attr-defined]
            widget.setPalette(self.palette())
            widget.setStyleSheet(self.stylesheet())
        elif isinstance(widget, QtWidgets.QWidget):  # type: ignore[attr-defined]
            widget.setPalette(self.palette())
            widget.setStyleSheet(self.stylesheet())

    def with_background(self, path: Path) -> "Theme":
        return replace(self, background_image=path)


try:
    from PySide6 import QtWidgets
except ImportError:  # pragma: no cover - handled by runtime environment
    QtWidgets = None  # type: ignore


__all__ = ["Theme"]
