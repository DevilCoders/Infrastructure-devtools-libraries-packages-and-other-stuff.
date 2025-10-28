"""Application entry point for the Infrastructure Manager GUI."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from PyQt6 import QtCore, QtWidgets

from .core.state import ApplicationState
from .ui.main_window import MainWindow
from .ui.theme import Theme
from .bootstrap import configure_qt_attributes


class InfraManagerApplication(QtWidgets.QApplication):
    """High level application object.

    The class is responsible for initializing the shared :class:`ApplicationState`
    and injecting it into the root :class:`MainWindow`. The application class also
    provides convenience helpers to update the global theme.
    """

    def __init__(self, background: Optional[Path] = None) -> None:
        configure_qt_attributes()
        super().__init__()
        self.setApplicationName("Infra Manager Studio")
        self.setAttribute(QtCore.Qt.ApplicationAttribute.AA_DontCreateNativeWidgetSiblings, True)
        self._state = ApplicationState.load()
        self._theme = Theme.default()
        if background:
            self._theme = self._theme.with_background(background)
        self._window = MainWindow(self._state, self._theme)
        self._theme.apply(self)

    def run(self) -> int:
        """Show the main window and start the Qt event loop."""
        self._window.show()
        return self.exec()


def main(background: Optional[str] = None) -> int:
    """Launch the GUI application.

    Parameters
    ----------
    background:
        Optional path to a background image that will be applied to the main
        window. Relative paths are resolved from the current working directory.
    """

    path = Path(background).expanduser().resolve() if background else None
    app = InfraManagerApplication(path)
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())
