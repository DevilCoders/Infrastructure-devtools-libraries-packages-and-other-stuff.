"""Advanced AI laboratory panel for training and dataset operations."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets

from ...core.state import AITrainingProfile, DatasetAsset


class AILabPanel(QtWidgets.QWidget):
    """Curate advanced training workloads and dataset preparation."""

    def __init__(
        self,
        profiles: Iterable[AITrainingProfile],
        datasets: Iterable[DatasetAsset],
    ) -> None:
        super().__init__()
        self._profiles = list(profiles)
        self._datasets = list(datasets)
        self._build_ui()

    # ------------------------------------------------------------------
    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)

        title = QtWidgets.QLabel(
            "Design and launch distributed training waves, toggle accelerator mixes, "
            "and craft production-ready datasets with governance baked in."
        )
        title.setWordWrap(True)
        layout.addWidget(title)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal, self)
        splitter.setChildrenCollapsible(False)

        splitter.addWidget(self._build_profile_panel())
        splitter.addWidget(self._build_dataset_panel())
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 4)

        layout.addWidget(splitter)

        footer = QtWidgets.QLabel(
            "Combine CPU-only warmups with GPU bursts, orchestrate LoRA fine-tunes, "
            "and continuously refine datasets through automated validation tasks."
        )
        footer.setWordWrap(True)
        footer.setStyleSheet("color: #C0C0C0;")
        layout.addWidget(footer)

    # ------------------------------------------------------------------
    def _build_profile_panel(self) -> QtWidgets.QWidget:
        container = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        header = QtWidgets.QLabel("Training Profiles & Parallel Strategies")
        header.setStyleSheet("font-weight: bold; color: #FF3355;")
        layout.addWidget(header)

        tree = QtWidgets.QTreeWidget(container)
        tree.setColumnCount(5)
        tree.setHeaderLabels(
            ["Profile", "Accelerator", "Parallelism", "Optimizer", "Fine-tuning"]
        )
        tree.setRootIsDecorated(False)
        tree.setUniformRowHeights(True)
        tree.setAlternatingRowColors(True)
        tree.header().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tree.itemSelectionChanged.connect(self._on_profile_selected)

        for profile in self._profiles:
            item = QtWidgets.QTreeWidgetItem(
                [
                    profile.name,
                    profile.accelerator,
                    profile.parallelism,
                    profile.optimizer,
                    profile.fine_tuning,
                ]
            )
            item.setData(0, QtCore.Qt.ItemDataRole.UserRole, profile)
            item.setToolTip(0, profile.status)
            tree.addTopLevelItem(item)

        layout.addWidget(tree)

        self._profile_detail = QtWidgets.QTextBrowser(container)
        self._profile_detail.setOpenExternalLinks(True)
        self._profile_detail.setPlaceholderText("Select a profile to review status and tuning notes.")
        self._profile_detail.setMaximumHeight(160)
        layout.addWidget(self._profile_detail)

        return container

    # ------------------------------------------------------------------
    def _build_dataset_panel(self) -> QtWidgets.QWidget:
        container = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        header = QtWidgets.QLabel("Dataset Factory & Quality Gates")
        header.setStyleSheet("font-weight: bold; color: #FF3355;")
        layout.addWidget(header)

        tree = QtWidgets.QTreeWidget(container)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Dataset", "Domain", "Formats", "Quality"])
        tree.setRootIsDecorated(False)
        tree.setUniformRowHeights(True)
        tree.setAlternatingRowColors(True)
        tree.header().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tree.itemSelectionChanged.connect(self._on_dataset_selected)

        for dataset in self._datasets:
            item = QtWidgets.QTreeWidgetItem(
                [
                    dataset.name,
                    dataset.domain,
                    ", ".join(dataset.formats),
                    dataset.quality,
                ]
            )
            item.setData(0, QtCore.Qt.ItemDataRole.UserRole, dataset)
            item.setToolTip(0, "Tasks: " + ", ".join(dataset.tasks))
            tree.addTopLevelItem(item)

        layout.addWidget(tree)

        self._dataset_detail = QtWidgets.QTextBrowser(container)
        self._dataset_detail.setPlaceholderText(
            "Select a dataset to inspect supported tasks, format curation, and automation steps."
        )
        layout.addWidget(self._dataset_detail)

        checklist = QtWidgets.QListWidget(container)
        checklist.setAlternatingRowColors(True)
        checklist.addItems(
            [
                "Run schema validation and drift detection",
                "Launch automated PII scrubbing pipelines",
                "Generate synthetic augmentations for rare events",
                "Publish dataset manifest to model registry",
            ]
        )
        checklist.setToolTip("Operational checklist for production-ready datasets.")
        layout.addWidget(checklist)

        return container

    # ------------------------------------------------------------------
    def _on_profile_selected(self) -> None:
        tree: QtWidgets.QTreeWidget = self.sender()  # type: ignore[assignment]
        items = tree.selectedItems()
        if not items:
            self._profile_detail.clear()
            return
        profile: AITrainingProfile = items[0].data(0, QtCore.Qt.ItemDataRole.UserRole)
        self._profile_detail.setHtml(
            f"""
            <h3 style='color:#FF3355;'>{profile.name}</h3>
            <p>Status: <b>{profile.status}</b></p>
            <p>Accelerator Mix: {profile.accelerator}</p>
            <p>Parallelism Strategy: {profile.parallelism}</p>
            <p>Optimizer Stack: {profile.optimizer}</p>
            <p>Fine-tuning Focus: {profile.fine_tuning}</p>
            """
        )

    # ------------------------------------------------------------------
    def _on_dataset_selected(self) -> None:
        tree: QtWidgets.QTreeWidget = self.sender()  # type: ignore[assignment]
        items = tree.selectedItems()
        if not items:
            self._dataset_detail.clear()
            return
        dataset: DatasetAsset = items[0].data(0, QtCore.Qt.ItemDataRole.UserRole)
        tasks = "".join(f"<li>{task}</li>" for task in dataset.tasks)
        self._dataset_detail.setHtml(
            f"""
            <h3 style='color:#FF3355;'>{dataset.name}</h3>
            <p>Domain: <b>{dataset.domain}</b></p>
            <p>Supported Formats: {', '.join(dataset.formats)}</p>
            <p>Quality Gate: {dataset.quality}</p>
            <p>Production Tasks:</p>
            <ul>{tasks}</ul>
            """
        )


__all__ = ["AILabPanel"]
