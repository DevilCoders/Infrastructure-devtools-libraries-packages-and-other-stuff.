"""Embedded UI resources such as the global stylesheet."""
from __future__ import annotations

NEON_STYLESHEET = r"""
/* Root window and global colors */
QWidget {
    background-color: $background;
    color: $text;
    font-family: "Segoe UI", "Inter", "Roboto", sans-serif;
    font-size: 14px;
    $backgroundImage
}

QMainWindow {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 rgba(9, 5, 32, 0.95),
        stop: 1 rgba(10, 10, 25, 0.92)
    );
}

QFrame#frostedContainer {
    background-color: rgba(255, 255, 255, 0.04);
    border-radius: ${borderRadius}px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(24px);
}

/* Tab widget styling */
QTabWidget::pane {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: ${borderRadius}px;
    background-color: rgba(15, 15, 35, 0.85);
    padding: 12px;
}

QTabBar::tab {
    background: transparent;
    color: $mutedText;
    padding: 10px 20px;
    margin: 0 8px;
    border-radius: ${borderRadius}px ${borderRadius}px 0 0;
    border: 1px solid transparent;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

QTabBar::tab:hover {
    color: $text;
    border-color: rgba(255, 255, 255, 0.1);
}

QTabBar::tab:selected {
    color: $text;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 rgba(255, 0, 64, 0.9),
        stop: 1 rgba(128, 0, 255, 0.9)
    );
    border: 1px solid rgba(255, 255, 255, 0.12);
}

/* Toolbar */
QToolBar {
    background: rgba(8, 8, 20, 0.85);
    border: none;
    padding: 6px 12px;
    spacing: 12px;
}

QToolButton {
    color: $text;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 rgba(255, 0, 64, 0.85),
        stop: 1 rgba(128, 0, 255, 0.85)
    );
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: ${borderRadius}px;
    padding: 8px 16px;
}

QToolButton:hover {
    border-color: rgba(255, 255, 255, 0.25);
}

QStatusBar {
    background: rgba(8, 8, 22, 0.9);
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}

/* Buttons */
QPushButton {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 $accent,
        stop: 1 $accentSecondary
    );
    color: $text;
    border-radius: ${borderRadius}px;
    padding: 8px 18px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    font-weight: 600;
}

QPushButton:hover {
    border-color: rgba(255, 255, 255, 0.3);
}

QPushButton:pressed {
    background: qlineargradient(
        x1: 0, y1: 1, x2: 1, y2: 0,
        stop: 0 $accent,
        stop: 1 rgba(90, 0, 210, 0.9)
    );
}

/* Inputs */
QLineEdit, QTextEdit, QListWidget, QTreeWidget, QTableWidget, QTextBrowser {
    background-color: rgba(18, 18, 38, 0.85);
    border-radius: ${borderRadius}px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 8px 12px;
    selection-background-color: rgba(255, 0, 64, 0.35);
    selection-color: $text;
}

QListWidget::item:selected, QTreeWidget::item:selected {
    background: rgba(255, 0, 64, 0.45);
}

QSplitter::handle {
    background: rgba(255, 255, 255, 0.04);
    border-radius: 2px;
}

/* Metric cards */
QFrame#metricCard {
    background: rgba(255, 255, 255, 0.03);
    border-radius: ${borderRadius}px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.45);
}

QLabel#metricTitle {
    color: $mutedText;
    letter-spacing: 0.3em;
}

QLabel#metricValue {
    color: $text;
    font-size: 34px;
    font-weight: 700;
}

/* Scrollbars */
QScrollBar:vertical {
    background: transparent;
    width: 16px;
    margin: 12px 0 12px 0;
}

QScrollBar::handle:vertical {
    background: rgba(255, 0, 64, 0.45);
    min-height: 40px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(255, 0, 64, 0.7);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: transparent;
    height: 0px;
}

QScrollBar:horizontal {
    background: transparent;
    height: 16px;
    margin: 0 12px 0 12px;
}

QScrollBar::handle:horizontal {
    background: rgba(128, 0, 255, 0.45);
    min-width: 40px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(128, 0, 255, 0.7);
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    background: transparent;
    width: 0px;
}

/* Headers */
QHeaderView::section {
    background: rgba(255, 255, 255, 0.04);
    color: $mutedText;
    border: none;
    padding: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    text-transform: uppercase;
    letter-spacing: 0.15em;
}

/* Tooltips */
QToolTip {
    background: rgba(15, 15, 35, 0.9);
    color: $text;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 6px 10px;
    border-radius: 6px;
}
"""

__all__ = ["NEON_STYLESHEET"]
