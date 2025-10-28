"""Repository list panel."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import Repository


class RepositoryPanel(QtWidgets.QGroupBox):
    """Displays known repositories with metadata."""

    repositorySelected = QtCore.Signal(Repository)

    def __init__(self, repositories: Iterable[Repository]) -> None:
        super().__init__("Repositories")
        self._repositories = list(repositories)
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.list_widget.itemSelectionChanged.connect(self._emit_selection)

        for repo in self._repositories:
            item = QtWidgets.QListWidgetItem(f"{repo.name} · {repo.platform}")
            item.setData(QtCore.Qt.ItemDataRole.UserRole, repo)
            item.setToolTip(repo.description)
            self.list_widget.addItem(item)

        layout.addWidget(self.list_widget)

        actions = QtWidgets.QHBoxLayout()
        open_button = QtWidgets.QPushButton("Open")
        open_button.clicked.connect(self._emit_open_current)
        actions.addWidget(open_button)

        tags_button = QtWidgets.QPushButton("Tags")
        tags_button.clicked.connect(self._show_tags)
        actions.addWidget(tags_button)

        actions.addStretch(1)
        layout.addLayout(actions)

    # ------------------------------------------------------------------
    def _emit_selection(self) -> None:
        item = self.list_widget.currentItem()
        if not item:
            return
        repository = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if repository:
            self.repositorySelected.emit(repository)

    def _emit_open_current(self) -> None:
        item = self.list_widget.currentItem()
        if not item:
            return
        repository = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if repository:
            self.repositorySelected.emit(repository)

    def _show_tags(self) -> None:
        item = self.list_widget.currentItem()
        if not item:
            QtWidgets.QMessageBox.information(self, "Tags", "Select a repository to view tags")
            return
        repository = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if repository:
            tags = ", ".join(repository.tags) or "No tags"
            QtWidgets.QMessageBox.information(self, repository.name, f"Tags: {tags}")


__all__ = ["RepositoryPanel"]
