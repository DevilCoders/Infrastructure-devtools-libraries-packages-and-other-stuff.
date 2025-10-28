"""Composite panel that manages infrastructure codebase modules and profiles."""
from __future__ import annotations

from typing import Iterable

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import pyqtSignal

from ...core.state import CodebaseModule, CodebaseProfile


class CodebaseManagerPanel(QtWidgets.QWidget):
    """Advanced management surface for infrastructure codebases."""

    moduleSelected = pyqtSignal(CodebaseModule)
    profileSaved = pyqtSignal(CodebaseProfile)

    def __init__(
        self,
        modules: Iterable[CodebaseModule],
        profiles: Iterable[CodebaseProfile],
    ) -> None:
        super().__init__()
        self._modules = list(modules)
        self._profiles = list(profiles)
        self._create_ui()
        self._populate_tree()
        self._populate_profile_table()

    # ------------------------------------------------------------------
    def _create_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(14)

        search_bar = QtWidgets.QLineEdit(self)
        search_bar.setPlaceholderText("Search modules, owners, or status…")
        search_bar.textChanged.connect(self._filter_modules)
        layout.addWidget(search_bar)
        self._search_bar = search_bar

        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal, self)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(10)
        layout.addWidget(splitter, 1)

        # Left tree ------------------------------------------------------
        tree_container = QtWidgets.QFrame(splitter)
        tree_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        tree_layout = QtWidgets.QVBoxLayout(tree_container)
        tree_layout.setContentsMargins(10, 10, 10, 10)
        tree_layout.setSpacing(8)

        tree_label = QtWidgets.QLabel("Codebase Modules")
        tree_label.setStyleSheet("font-weight: 600; text-transform: uppercase;")
        tree_layout.addWidget(tree_label)

        tree = QtWidgets.QTreeWidget(tree_container)
        tree.setHeaderLabels(["Module", "Owner", "Status", "Coverage"])
        tree.setAlternatingRowColors(True)
        tree.setRootIsDecorated(False)
        tree.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        tree.itemSelectionChanged.connect(self._emit_module_selection)
        tree_layout.addWidget(tree, 1)
        self._tree = tree

        controls = QtWidgets.QHBoxLayout()
        refresh_button = QtWidgets.QPushButton("Refresh Inventory")
        refresh_button.clicked.connect(self._refresh_tree)
        controls.addWidget(refresh_button)

        expand_button = QtWidgets.QPushButton("Expand All")
        expand_button.clicked.connect(tree.expandAll)
        controls.addWidget(expand_button)

        collapse_button = QtWidgets.QPushButton("Collapse")
        collapse_button.clicked.connect(tree.collapseAll)
        controls.addWidget(collapse_button)

        controls.addStretch(1)
        tree_layout.addLayout(controls)

        # Right side -----------------------------------------------------
        right_container = QtWidgets.QFrame(splitter)
        right_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        right_layout = QtWidgets.QVBoxLayout(right_container)
        right_layout.setContentsMargins(10, 10, 10, 10)
        right_layout.setSpacing(10)

        tabs = QtWidgets.QTabWidget(right_container)
        tabs.addTab(self._create_basic_tab(), "Basic")
        tabs.addTab(self._create_advanced_tab(), "Advanced")
        right_layout.addWidget(tabs)

        profile_group = QtWidgets.QGroupBox("Profile Matches")
        profile_layout = QtWidgets.QVBoxLayout(profile_group)
        profile_layout.setSpacing(8)

        table = QtWidgets.QTableWidget(0, 6, profile_group)
        table.setHorizontalHeaderLabels(
            [
                "Company",
                "Tier",
                "Project Manager",
                "Success Manager",
                "Active Modules",
                "Reliability",
            ]
        )
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        profile_layout.addWidget(table)
        self._profile_table = table

        right_layout.addWidget(profile_group, 1)

        action_bar = QtWidgets.QHBoxLayout()
        action_bar.addStretch(1)
        save_button = QtWidgets.QPushButton("Save")
        save_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogApplyButton))
        save_button.clicked.connect(self._save_profile)
        action_bar.addWidget(save_button)
        self._save_button = save_button

        reset_button = QtWidgets.QPushButton("Reset")
        reset_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_BrowserReload))
        reset_button.clicked.connect(self._reset_forms)
        action_bar.addWidget(reset_button)

        right_layout.addLayout(action_bar)

        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)

    # ------------------------------------------------------------------
    def _create_basic_tab(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(widget)
        layout.setHorizontalSpacing(16)
        layout.setVerticalSpacing(12)

        self._company_edit = QtWidgets.QLineEdit()
        self._company_edit.setPlaceholderText("Company or program name")
        layout.addRow("Company", self._company_edit)

        self._market_combo = QtWidgets.QComboBox()
        self._market_combo.addItems([
            "Enterprise",
            "Upper Mid-Market",
            "Mid-Market",
            "Digital Native",
            "Public Sector",
        ])
        layout.addRow("Market Tier", self._market_combo)

        self._project_combo = QtWidgets.QComboBox()
        self._project_combo.addItems([
            "Avery Castillo",
            "Jordan Singh",
            "Dakota Silva",
            "Parker Diaz",
            "Morgan Lee",
            "Remy Zhao",
        ])
        layout.addRow("Project Manager", self._project_combo)

        self._success_combo = QtWidgets.QComboBox()
        self._success_combo.addItems([
            "Remy Zhao",
            "Morgan Lee",
            "Kai Morgan",
            "Jamie Patel",
            "Lex Chen",
        ])
        layout.addRow("Success Manager", self._success_combo)

        self._module_spin = QtWidgets.QSpinBox()
        self._module_spin.setRange(0, 99)
        self._module_spin.setValue(12)
        layout.addRow("Active Modules", self._module_spin)

        self._reliability_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self._reliability_slider.setRange(0, 100)
        self._reliability_slider.setValue(90)
        layout.addRow("Reliability Target", self._reliability_slider)

        return widget

    # ------------------------------------------------------------------
    def _create_advanced_tab(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(12)

        controls_group = QtWidgets.QGroupBox("Automation & Governance")
        controls_layout = QtWidgets.QGridLayout(controls_group)
        controls_layout.setHorizontalSpacing(16)
        controls_layout.setVerticalSpacing(10)

        self._policy_check = QtWidgets.QCheckBox("Enforce policy packs")
        self._policy_check.setChecked(True)
        controls_layout.addWidget(self._policy_check, 0, 0, 1, 2)

        self._compliance_check = QtWidgets.QCheckBox("Enable compliance diff scanning")
        self._compliance_check.setChecked(True)
        controls_layout.addWidget(self._compliance_check, 1, 0, 1, 2)

        self._ci_checkbox = QtWidgets.QCheckBox("Trigger CI pipelines on plan change")
        self._ci_checkbox.setChecked(True)
        controls_layout.addWidget(self._ci_checkbox, 2, 0, 1, 2)

        self._ai_checkbox = QtWidgets.QCheckBox("Pair with AI runbook assistant")
        controls_layout.addWidget(self._ai_checkbox, 3, 0, 1, 2)

        coverage_label = QtWidgets.QLabel("Documentation Coverage")
        controls_layout.addWidget(coverage_label, 4, 0)

        self._doc_spin = QtWidgets.QSpinBox()
        self._doc_spin.setRange(0, 100)
        self._doc_spin.setSuffix(" %")
        self._doc_spin.setValue(80)
        controls_layout.addWidget(self._doc_spin, 4, 1)

        cadence_label = QtWidgets.QLabel("Release Cadence")
        controls_layout.addWidget(cadence_label, 5, 0)

        self._cadence_combo = QtWidgets.QComboBox()
        self._cadence_combo.addItems([
            "Weekly",
            "Bi-Weekly",
            "Monthly",
            "Quarterly",
        ])
        controls_layout.addWidget(self._cadence_combo, 5, 1)

        layout.addWidget(controls_group)

        notes_group = QtWidgets.QGroupBox("Notes")
        notes_layout = QtWidgets.QVBoxLayout(notes_group)
        self._notes_edit = QtWidgets.QPlainTextEdit()
        self._notes_edit.setPlaceholderText(
            "Document integrations, drift hotspots, or success playbooks…"
        )
        notes_layout.addWidget(self._notes_edit)
        layout.addWidget(notes_group, 1)

        return widget

    # ------------------------------------------------------------------
    def _populate_tree(self) -> None:
        self._tree.clear()

        categories: dict[str, QtWidgets.QTreeWidgetItem] = {}
        for module in self._modules:
            category_item = categories.get(module.category)
            if category_item is None:
                category_item = QtWidgets.QTreeWidgetItem([module.category])
                category_item.setFirstColumnSpanned(True)
                category_item.setFlags(
                    category_item.flags()
                    & ~QtCore.Qt.ItemFlag.ItemIsSelectable
                )
                self._tree.addTopLevelItem(category_item)
                categories[module.category] = category_item

            item = QtWidgets.QTreeWidgetItem(
                [
                    module.name,
                    module.owner,
                    module.status.title(),
                    f"{module.coverage}%",
                ]
            )
            item.setData(0, QtCore.Qt.ItemDataRole.UserRole, module)
            category_item.addChild(item)

        self._tree.expandAll()

    def _populate_profile_table(self) -> None:
        self._profile_table.setRowCount(0)
        for profile in self._profiles:
            row = self._profile_table.rowCount()
            self._profile_table.insertRow(row)
            self._profile_table.setItem(row, 0, QtWidgets.QTableWidgetItem(profile.company))
            self._profile_table.setItem(row, 1, QtWidgets.QTableWidgetItem(profile.market_tier))
            self._profile_table.setItem(row, 2, QtWidgets.QTableWidgetItem(profile.project_manager))
            self._profile_table.setItem(row, 3, QtWidgets.QTableWidgetItem(profile.success_manager))
            self._profile_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(profile.active_modules)))
            self._profile_table.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(f"{profile.reliability_score}%"),
            )

    # ------------------------------------------------------------------
    def _filter_modules(self, query: str) -> None:
        query = query.strip().lower()
        for i in range(self._tree.topLevelItemCount()):
            category_item = self._tree.topLevelItem(i)
            visible_children = 0
            for j in range(category_item.childCount()):
                item = category_item.child(j)
                module: CodebaseModule = item.data(0, QtCore.Qt.ItemDataRole.UserRole)
                is_visible = not query or any(
                    term.startswith(query)
                    for term in [
                        module.name.lower(),
                        module.owner.lower(),
                        module.status.lower(),
                    ]
                )
                item.setHidden(not is_visible)
                if is_visible:
                    visible_children += 1

            category_item.setHidden(visible_children == 0)

    def _refresh_tree(self) -> None:
        # In a real implementation this would pull fresh metadata from git providers.
        self._populate_tree()
        self._filter_modules(self._search_bar.text())

    def _emit_module_selection(self) -> None:
        selected_items = self._tree.selectedItems()
        if not selected_items:
            return
        module = selected_items[0].data(0, QtCore.Qt.ItemDataRole.UserRole)
        if module:
            self.moduleSelected.emit(module)

    def _save_profile(self) -> None:
        profile = CodebaseProfile(
            company=self._company_edit.text() or "Untitled Program",
            market_tier=self._market_combo.currentText(),
            project_manager=self._project_combo.currentText(),
            success_manager=self._success_combo.currentText(),
            active_modules=self._module_spin.value(),
            reliability_score=self._reliability_slider.value(),
        )
        self.profileSaved.emit(profile)

        row = self._profile_table.rowCount()
        self._profile_table.insertRow(row)
        self._profile_table.setItem(row, 0, QtWidgets.QTableWidgetItem(profile.company))
        self._profile_table.setItem(row, 1, QtWidgets.QTableWidgetItem(profile.market_tier))
        self._profile_table.setItem(row, 2, QtWidgets.QTableWidgetItem(profile.project_manager))
        self._profile_table.setItem(row, 3, QtWidgets.QTableWidgetItem(profile.success_manager))
        self._profile_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(profile.active_modules)))
        self._profile_table.setItem(
            row,
            5,
            QtWidgets.QTableWidgetItem(f"{profile.reliability_score}%"),
        )

        self._save_button.setEnabled(False)
        QtCore.QTimer.singleShot(800, lambda: self._save_button.setEnabled(True))

    def _reset_forms(self) -> None:
        self._company_edit.clear()
        self._market_combo.setCurrentIndex(0)
        self._project_combo.setCurrentIndex(0)
        self._success_combo.setCurrentIndex(0)
        self._module_spin.setValue(12)
        self._reliability_slider.setValue(90)
        self._policy_check.setChecked(True)
        self._compliance_check.setChecked(True)
        self._ci_checkbox.setChecked(True)
        self._ai_checkbox.setChecked(False)
        self._doc_spin.setValue(80)
        self._cadence_combo.setCurrentIndex(0)
        self._notes_edit.clear()


__all__ = ["CodebaseManagerPanel"]
