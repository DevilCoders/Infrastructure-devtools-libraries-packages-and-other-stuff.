"""Panel presenting advanced feature catalog."""
from __future__ import annotations

from typing import Dict, Iterable, List

from PyQt6 import QtCore, QtWidgets

from ...core.state import AdvancedFeature, InfrastructureTarget


class AdvancedFeaturePanel(QtWidgets.QWidget):
    """Display a matrix of advanced capabilities bundled with the studio."""

    def __init__(
        self,
        features: Iterable[AdvancedFeature],
        infrastructures: Iterable[InfrastructureTarget],
    ) -> None:
        super().__init__()
        self._features = list(features)
        self._infrastructures = list(infrastructures)
        self._table_targets: Dict[QtWidgets.QTableWidget, List[InfrastructureTarget]] = {}
        self._detail_browser: QtWidgets.QTextBrowser | None = None
        self._operation_selector: QtWidgets.QComboBox | None = None
        self._execute_button: QtWidgets.QPushButton | None = None
        self._active_target: InfrastructureTarget | None = None
        self._manager_tabs: QtWidgets.QTabWidget | None = None
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)

        header = QtWidgets.QLabel(
            "Explore more than thirty advanced operator-centric capabilities,\n"
            "from concurrency orchestration to governance guardrails."
        )
        header.setWordWrap(True)
        layout.addWidget(header)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical, self)
        layout.addWidget(splitter)

        tree_frame = QtWidgets.QFrame(splitter)
        tree_layout = QtWidgets.QVBoxLayout(tree_frame)
        tree_layout.setContentsMargins(0, 0, 0, 0)
        tree_layout.setSpacing(8)

        tree = QtWidgets.QTreeWidget(tree_frame)
        tree.setColumnCount(4)
        tree.setHeaderLabels(["Feature", "Category", "Description", "Status"])
        tree.setRootIsDecorated(False)
        tree.setAlternatingRowColors(True)
        tree.setUniformRowHeights(True)

        for feature in self._features:
            item = QtWidgets.QTreeWidgetItem(
                [feature.name, feature.category, feature.description, feature.status]
            )
            tree.addTopLevelItem(item)

        header_view = tree.header()
        header_view.setStretchLastSection(True)
        header_view.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_view.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        tree_layout.addWidget(tree)

        manager_frame = QtWidgets.QFrame(splitter)
        manager_layout = QtWidgets.QVBoxLayout(manager_frame)
        manager_layout.setContentsMargins(0, 0, 0, 0)
        manager_layout.setSpacing(10)

        manager_header = QtWidgets.QLabel(
            "Command heterogeneous infrastructure estates directly from this advanced control center."
        )
        manager_header.setWordWrap(True)
        manager_layout.addWidget(manager_header)

        self._manager_tabs = QtWidgets.QTabWidget(manager_frame)
        self._manager_tabs.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self._manager_tabs.setDocumentMode(True)
        manager_layout.addWidget(self._manager_tabs)

        self._operation_selector = QtWidgets.QComboBox(manager_frame)
        self._operation_selector.setPlaceholderText("Select an orchestration action…")
        self._operation_selector.setEnabled(False)

        self._execute_button = QtWidgets.QPushButton("Execute Operation", manager_frame)
        self._execute_button.setEnabled(False)
        self._execute_button.clicked.connect(self._execute_operation)

        control_bar = QtWidgets.QHBoxLayout()
        control_bar.addWidget(self._operation_selector, 1)
        control_bar.addWidget(self._execute_button)
        control_bar.addStretch(1)
        manager_layout.addLayout(control_bar)

        self._detail_browser = QtWidgets.QTextBrowser(manager_frame)
        self._detail_browser.setOpenExternalLinks(True)
        self._detail_browser.setPlaceholderText(
            "Select an infrastructure surface to inspect runbooks, endpoints, and lifecycle history."
        )
        manager_layout.addWidget(self._detail_browser)

        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)

        self._populate_infrastructure_tabs()

    # ------------------------------------------------------------------
    def _populate_infrastructure_tabs(self) -> None:
        if not self._manager_tabs:
            return

        tab_definitions = [
            (
                "VPS Fleets",
                "vps",
                "Track bare metal and VPS clusters spanning edge and network gateways.",
            ),
            (
                "Container Platforms",
                "container",
                "Monitor Kubernetes and container platform workloads with rollout tooling.",
            ),
            (
                "Local Environments",
                "local",
                "Coordinate operator laptops, lab appliances, and self-hosted sandboxes.",
            ),
        ]

        for title, kind, blurb in tab_definitions:
            tab = self._create_infrastructure_tab(kind, blurb)
            self._manager_tabs.addTab(tab, title)

        if self._manager_tabs.count():
            self._manager_tabs.setCurrentIndex(0)

    def _create_infrastructure_tab(self, kind: str, blurb: str) -> QtWidgets.QWidget:
        wrapper = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(wrapper)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        description = QtWidgets.QLabel(blurb)
        description.setWordWrap(True)
        layout.addWidget(description)

        table = QtWidgets.QTableWidget(wrapper)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Name", "Environment", "Region", "Status", "Owner"])
        table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        table.setAlternatingRowColors(True)
        table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        entries = [infra for infra in self._infrastructures if infra.kind == kind]
        table.setRowCount(len(entries))

        for row, target in enumerate(entries):
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(target.name))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(target.environment))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(target.region))
            table.setItem(row, 3, QtWidgets.QTableWidgetItem(target.status))
            table.setItem(row, 4, QtWidgets.QTableWidgetItem(target.owner))

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        table.itemSelectionChanged.connect(lambda table=table: self._on_infrastructure_selected(table))

        layout.addWidget(table)
        self._table_targets[table] = entries
        return wrapper

    def _on_infrastructure_selected(self, table: QtWidgets.QTableWidget) -> None:
        targets = self._table_targets.get(table, [])
        row = table.currentRow()
        if row < 0 or row >= len(targets):
            self._active_target = None
            if self._detail_browser:
                self._detail_browser.clear()
            if self._operation_selector and self._execute_button:
                self._operation_selector.clear()
                self._operation_selector.setEnabled(False)
                self._execute_button.setEnabled(False)
            return

        target = targets[row]
        self._active_target = target

        if self._detail_browser:
            self._detail_browser.setHtml(self._render_infrastructure_detail(target))

        if not self._operation_selector or not self._execute_button:
            return

        self._operation_selector.blockSignals(True)
        self._operation_selector.clear()
        for op in target.operations:
            self._operation_selector.addItem(op)
        self._operation_selector.setEnabled(bool(target.operations))
        self._operation_selector.blockSignals(False)
        self._execute_button.setEnabled(bool(target.operations))

    def _render_infrastructure_detail(self, target: InfrastructureTarget) -> str:
        endpoints = "".join(
            f"<li><code>{endpoint}</code></li>" for endpoint in target.endpoints
        ) or "<li><em>No endpoints registered.</em></li>"
        operations = "".join(
            f"<li>{operation}</li>" for operation in target.operations
        ) or "<li><em>No automated operations available.</em></li>"
        automation = (
            f"<code>{target.automation}</code>" if target.automation else "<em>None provided</em>"
        )
        return (
            f"<h3 style='color:#FF0040;'>{target.name}</h3>"
            f"<p><b>Environment:</b> {target.environment} &mdash; <b>Region:</b> {target.region}</p>"
            f"<p><b>Current status:</b> {target.status} &nbsp;|&nbsp; <b>Owner:</b> {target.owner}</p>"
            f"<p><b>Automation entrypoint:</b> {automation}</p>"
            f"<p><b>Primary endpoints</b></p><ul>{endpoints}</ul>"
            f"<p><b>Orchestration playbooks</b></p><ul>{operations}</ul>"
            "<p style='color:rgba(255,255,255,0.65);'>Select a row and choose an operation to orchestrate directly from the console.</p>"
        )

    def _execute_operation(self) -> None:
        if not (self._active_target and self._operation_selector and self._execute_button):
            return
        operation = self._operation_selector.currentText()
        if not operation:
            return

        confirmation = (
            f"<p>Queued <b>{operation}</b> for <b>{self._active_target.name}</b> "
            f"in <code>{self._active_target.environment}</code>.</p>"
        )
        if self._detail_browser:
            self._detail_browser.append(
                f"<p style='color:#7CFC00;'>Automation scheduled: {operation} → {self._active_target.name}</p>"
            )

        QtWidgets.QMessageBox.information(
            self,
            "Operation Scheduled",
            confirmation,
        )


__all__ = ["AdvancedFeaturePanel"]
