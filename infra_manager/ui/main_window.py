"""Main window composition."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PyQt6 import QtCore, QtGui, QtWidgets

from ..core.state import (
    ApplicationState,
    CodebaseModule,
    CodebaseProfile,
    CommandCenterTab,
    ConfigurationTemplate,
    DeploymentProfile,
    Repository,
)
from .theme import Theme
from .widgets.cards import MetricCard
from .widgets.pipeline_panel import PipelinePanel
from .widgets.repo_panel import RepositoryPanel
from .widgets.codebase_manager_panel import CodebaseManagerPanel
from .widgets.capability_panel import CapabilityPanel
from .widgets.workflow_panel import WorkflowPanel
from .widgets.cluster_panel import ClusterPanel
from .widgets.performance_panel import PerformancePanel
from .widgets.vps_panel import VPSPanel
from .widgets.deployment_panel import DeploymentPanel
from .widgets.config_panel import ConfigurationPanel
from .widgets.advanced_feature_panel import AdvancedFeaturePanel
from .widgets.observability_panel import ObservabilityPanel
from .widgets.security_panel import SecurityPanel
from .widgets.automation_panel import AutomationPanel
from .widgets.scheduler_panel import SchedulerPanel
from .widgets.async_jobs_panel import AsyncJobsPanel
from .widgets.batch_panel import BatchPanel
from .widgets.notification_panel import NotificationPanel
from .widgets.access_panel import AccessPanel
from .widgets.runbook_panel import RunbookPanel
from .widgets.blueprint_panel import BlueprintPanel
from .widgets.data_pipeline_panel import DataPipelinePanel
from .widgets.service_mesh_panel import ServiceMeshPanel
from .widgets.cost_panel import CostPanel
from .widgets.tenant_panel import TenantPanel
from .widgets.logging_panel import LoggingPanel
from .widgets.ai_assistant_panel import AIAssistantPanel
from .widgets.ai_model_panel import AIModelPanel
from .widgets.ai_workflow_panel import AIWorkflowPanel
from .widgets.ai_training_panel import AITrainingPanel
from .widgets.ai_integration_panel import AIIntegrationPanel
from .widgets.ai_lab_panel import AILabPanel
from .widgets.code_lab_panel import CodeLabPanel


class MainWindow(QtWidgets.QMainWindow):
    """Root window containing all panels and navigation widgets."""

    def __init__(self, state: ApplicationState, theme: Theme) -> None:
        super().__init__()
        self.state = state
        self.theme = theme
        self._command_center_lookup: dict[int, CommandCenterTab] = {}

        self.setWindowTitle("Infra Manager Studio")
        self.resize(1400, 900)
        self.setMinimumSize(1024, 640)
        self.setWindowIcon(QtGui.QIcon.fromTheme("applications-system"))

        self._create_central_widget()
        self._create_toolbar()
        self._create_status_bar()
        self.theme.apply(self)

        self._animate_startup()

    # ------------------------------------------------------------------
    def _create_central_widget(self) -> None:
        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = QtWidgets.QTabWidget(central)
        self._command_center_lookup.clear()
        self.tabs.addTab(self._create_overview_tab(), "Overview")
        self.tabs.addTab(self._create_repository_tab(), "Repositories")
        self.tabs.addTab(self._create_codebase_manager_tab(), "Codebase Manager")
        self.tabs.addTab(self._create_pipeline_tab(), "Pipelines")
        self.tabs.addTab(self._create_workflow_tab(), "Workflows")
        self.tabs.addTab(self._create_performance_tab(), "Performance")
        self.tabs.addTab(self._create_cluster_tab(), "Clusters")
        self.tabs.addTab(self._create_vps_tab(), "VPS")
        self.tabs.addTab(self._create_deployment_tab(), "Local Deploy")
        self.tabs.addTab(self._create_configuration_tab(), "Configurations")
        self.tabs.addTab(self._create_advanced_features_tab(), "Advanced")
        self.tabs.addTab(self._create_ai_assistant_tab(), "AI Assistants")
        self.tabs.addTab(self._create_ai_model_tab(), "AI Models")
        self.tabs.addTab(self._create_ai_workflow_tab(), "AI Workflows")
        self.tabs.addTab(self._create_ai_training_tab(), "AI Training")
        self.tabs.addTab(self._create_ai_lab_tab(), "AI Lab")
        self.tabs.addTab(self._create_ai_integration_tab(), "AI Integrations")
        self.tabs.addTab(self._create_observability_tab(), "Observability")
        self.tabs.addTab(self._create_security_tab(), "Security")
        self.tabs.addTab(self._create_automation_tab(), "Automation")
        self.tabs.addTab(self._create_code_lab_tab(), "Code Lab")
        self.tabs.addTab(self._create_scheduler_tab(), "Cron & Schedules")
        self.tabs.addTab(self._create_async_jobs_tab(), "Async Jobs")
        self.tabs.addTab(self._create_batch_tab(), "Bulk Ops")
        self.tabs.addTab(self._create_notification_tab(), "Notifications")
        self.tabs.addTab(self._create_access_tab(), "Access")
        self.tabs.addTab(self._create_runbook_tab(), "Runbooks")
        self.tabs.addTab(self._create_blueprint_tab(), "Blueprints")
        self.tabs.addTab(self._create_data_pipeline_tab(), "Data Pipelines")
        self.tabs.addTab(self._create_service_mesh_tab(), "Service Mesh")
        self.tabs.addTab(self._create_cost_tab(), "Cost")
        self.tabs.addTab(self._create_tenant_tab(), "Tenants")
        self.tabs.addTab(self._create_logging_tab(), "Logging")

        for descriptor in self.state.command_center_tabs:
            widget = self._create_command_center_tab(descriptor)
            index = self.tabs.addTab(widget, descriptor.title)
            self.tabs.setTabToolTip(index, descriptor.description)
            self._command_center_lookup[index] = descriptor

        self.tabs.currentChanged.connect(self._handle_tab_changed)

        layout.addWidget(self.tabs)
        self.setCentralWidget(central)

    def _create_overview_tab(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setSpacing(14)

        metrics = QtWidgets.QHBoxLayout()
        metrics.addWidget(MetricCard("Repositories", len(self.state.repositories)))
        metrics.addWidget(MetricCard("Pipelines", len(self.state.pipelines)))
        metrics.addWidget(MetricCard("Workflows", len(self.state.workflows)))
        metrics.addWidget(MetricCard("Clusters", len(self.state.clusters)))
        metrics.addWidget(MetricCard("VPS", len(self.state.servers)))
        metrics.addStretch(1)
        layout.addLayout(metrics)

        intro = QtWidgets.QTextBrowser(widget)
        intro.setOpenExternalLinks(True)
        intro.setHtml(
            """
            <h2 style='color:#FF0040;'>Infrastructure Command Studio</h2>
            <p>Track repository hygiene, orchestrate CI/CD flows, and operate clusters
            from a single neon-dark cockpit. Tabs along the top segment workflows
            for repositories, pipelines, observability, and runtime tuning.</p>
            <p>Extend via <b>Configurations</b> to drop custom manifests, policies, and
            automation recipes directly into your managed mono-repos.</p>
            """
        )
        layout.addWidget(intro)

        return widget

    def _create_repository_tab(self) -> QtWidgets.QWidget:
        panel = RepositoryPanel(self.state.repositories.values())
        panel.repositorySelected.connect(self._on_repository_selected)
        return panel

    def _create_codebase_manager_tab(self) -> QtWidgets.QWidget:
        panel = CodebaseManagerPanel(
            self.state.codebase_modules,
            self.state.codebase_profiles,
        )
        panel.moduleSelected.connect(self._on_codebase_module_selected)
        panel.profileSaved.connect(self._on_codebase_profile_saved)
        return panel

    def _create_pipeline_tab(self) -> QtWidgets.QWidget:
        panel = PipelinePanel(self.state.pipelines)
        panel.pipelineTriggered.connect(self._on_pipeline_triggered)
        return panel

    def _create_workflow_tab(self) -> QtWidgets.QWidget:
        panel = WorkflowPanel(self.state.workflows)
        panel.workflowRequested.connect(self._on_workflow_requested)
        return panel

    def _create_performance_tab(self) -> QtWidgets.QWidget:
        return PerformancePanel(self.state.performance)

    def _create_cluster_tab(self) -> QtWidgets.QWidget:
        return ClusterPanel(self.state.clusters)

    def _create_vps_tab(self) -> QtWidgets.QWidget:
        panel = VPSPanel(self.state.servers)
        panel.serverActionRequested.connect(self._on_server_action)
        return panel

    def _create_deployment_tab(self) -> QtWidgets.QWidget:
        panel = DeploymentPanel(self.state.deployments)
        panel.deploymentRequested.connect(self._on_deployment_requested)
        return panel

    def _create_configuration_tab(self) -> QtWidgets.QWidget:
        panel = ConfigurationPanel(self.state.configurations)
        panel.templateSelected.connect(self._on_template_selected)
        return panel

    def _create_advanced_features_tab(self) -> QtWidgets.QWidget:
        return AdvancedFeaturePanel(self.state.advanced_features)

    def _create_observability_tab(self) -> QtWidgets.QWidget:
        return ObservabilityPanel(self.state.probes)

    def _create_security_tab(self) -> QtWidgets.QWidget:
        return SecurityPanel(self.state.security_policies)

    def _create_automation_tab(self) -> QtWidgets.QWidget:
        return AutomationPanel(self.state.automation_scripts)

    def _create_code_lab_tab(self) -> QtWidgets.QWidget:
        return CodeLabPanel(self.state.code_workspaces)

    def _create_scheduler_tab(self) -> QtWidgets.QWidget:
        return SchedulerPanel(self.state.cron_schedules)

    def _create_async_jobs_tab(self) -> QtWidgets.QWidget:
        return AsyncJobsPanel(self.state.async_jobs)

    def _create_batch_tab(self) -> QtWidgets.QWidget:
        return BatchPanel(self.state.batch_processes)

    def _create_notification_tab(self) -> QtWidgets.QWidget:
        return NotificationPanel(self.state.notification_channels)

    def _create_access_tab(self) -> QtWidgets.QWidget:
        return AccessPanel(self.state.access_profiles)

    def _create_runbook_tab(self) -> QtWidgets.QWidget:
        return RunbookPanel(self.state.runbooks)

    def _create_blueprint_tab(self) -> QtWidgets.QWidget:
        return BlueprintPanel(self.state.blueprints)

    def _create_data_pipeline_tab(self) -> QtWidgets.QWidget:
        return DataPipelinePanel(self.state.data_pipelines)

    def _create_service_mesh_tab(self) -> QtWidgets.QWidget:
        return ServiceMeshPanel(self.state.mesh_policies)

    def _create_cost_tab(self) -> QtWidgets.QWidget:
        return CostPanel(self.state.cost_strategies)

    def _create_tenant_tab(self) -> QtWidgets.QWidget:
        return TenantPanel(self.state.tenants)

    def _create_logging_tab(self) -> QtWidgets.QWidget:
        return LoggingPanel(self.state.logging_sinks)

    def _create_ai_assistant_tab(self) -> QtWidgets.QWidget:
        return AIAssistantPanel(self.state.ai_assistants)

    def _create_ai_model_tab(self) -> QtWidgets.QWidget:
        return AIModelPanel(self.state.ai_models)

    def _create_ai_workflow_tab(self) -> QtWidgets.QWidget:
        return AIWorkflowPanel(self.state.ai_workflows)

    def _create_ai_training_tab(self) -> QtWidgets.QWidget:
        return AITrainingPanel(self.state.ai_training_runs)

    def _create_ai_integration_tab(self) -> QtWidgets.QWidget:
        return AIIntegrationPanel(self.state.ai_integrations)

    def _create_ai_lab_tab(self) -> QtWidgets.QWidget:
        return AILabPanel(self.state.ai_training_profiles, self.state.dataset_assets)

    def _create_command_center_tab(self, descriptor: CommandCenterTab) -> QtWidgets.QWidget:
        return CapabilityPanel(descriptor)

    # ------------------------------------------------------------------
    def _create_toolbar(self) -> None:
        toolbar = QtWidgets.QToolBar("Quick Actions", self)
        toolbar.setMovable(False)
        toolbar.setIconSize(QtCore.QSize(20, 20))

        refresh_action = QtGui.QAction("Refresh", self)
        refresh_action.setIcon(QtGui.QIcon.fromTheme("view-refresh"))
        refresh_action.triggered.connect(lambda: self.statusBar().showMessage("Refreshing state...", 3000))

        theme_action = QtGui.QAction("Toggle Neon", self)
        theme_action.setCheckable(True)
        theme_action.triggered.connect(self._toggle_neon_mode)

        toolbar.addAction(refresh_action)
        toolbar.addAction(theme_action)
        toolbar.addSeparator()

        background_action = QtGui.QAction("Set Background", self)
        background_action.triggered.connect(self._select_background_image)
        toolbar.addAction(background_action)

        self.addToolBar(toolbar)

    def _create_status_bar(self) -> None:
        status = QtWidgets.QStatusBar(self)
        status.showMessage("Ready")
        self.setStatusBar(status)

    # ------------------------------------------------------------------
    def _toggle_neon_mode(self, checked: bool) -> None:
        neon = Theme(
            background_color="#050505" if checked else self.theme.background_color,
            accent_color="#FF0040" if checked else self.theme.accent_color,
            text_color="#F5F5F5",
            card_color="#1A1A1A",
            border_radius=14,
            background_image=self.theme.background_image,
        )
        self.theme = neon
        self.theme.apply(self)
        self._animate_palette()

    def _select_background_image(self) -> None:
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilters(["Images (*.png *.jpg *.jpeg)"])
        if file_dialog.exec():
            selected: Iterable[str] = file_dialog.selectedFiles()
            for path in selected:
                self.theme = self.theme.with_background(Path(path))
                self.theme.apply(self)
                self.statusBar().showMessage(f"Applied background: {path}", 4000)
                break

    # ------------------------------------------------------------------
    def _animate_startup(self) -> None:
        self._fade_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._fade_effect)
        animation = QtCore.QPropertyAnimation(self._fade_effect, b"opacity", self)
        animation.setDuration(900)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    def _animate_palette(self) -> None:
        animation = QtCore.QVariantAnimation(self)
        animation.setDuration(600)
        start_color = QtGui.QColor(self.palette().color(QtGui.QPalette.Window))
        end_color = QtGui.QColor(self.theme.background_color)
        animation.setStartValue(start_color)
        animation.setEndValue(end_color)

        def update(value: QtGui.QColor) -> None:
            palette = self.palette()
            palette.setColor(QtGui.QPalette.Window, value)
            self.setPalette(palette)

        animation.valueChanged.connect(update)
        animation.finished.connect(lambda: self.theme.apply(self))
        animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    # ------------------------------------------------------------------
    def _on_repository_selected(self, repository: Repository) -> None:
        self.statusBar().showMessage(f"Selected repo: {repository.name} ({repository.platform})", 5000)

    def _on_pipeline_triggered(self, pipeline: str) -> None:
        self.statusBar().showMessage(f"Triggering pipeline: {pipeline}", 5000)

    def _on_workflow_requested(self, workflow: str) -> None:
        self.statusBar().showMessage(f"Workflow requested: {workflow}", 5000)

    def _on_server_action(self, action: str, target: str) -> None:
        self.statusBar().showMessage(f"{action.title()} server {target}", 5000)

    def _on_deployment_requested(self, profile: DeploymentProfile) -> None:
        self.statusBar().showMessage(
            f"Launching local deployment '{profile.name}' targeting {profile.target}", 6000
        )

    def _on_template_selected(self, template: ConfigurationTemplate) -> None:
        self.statusBar().showMessage(
            f"Loaded configuration template: {template.name} ({template.version})", 5000
        )

    def _on_codebase_module_selected(self, module: CodebaseModule) -> None:
        self.statusBar().showMessage(
            f"Focused module: {module.name} owned by {module.owner}",
            5000,
        )

    def _on_codebase_profile_saved(self, profile: CodebaseProfile) -> None:
        self.statusBar().showMessage(
            f"Saved profile for {profile.company} targeting {profile.market_tier}",
            5000,
        )

    def _handle_tab_changed(self, index: int) -> None:
        descriptor = self._command_center_lookup.get(index)
        if descriptor:
            self.statusBar().showMessage(
                f"Viewing {descriptor.title}: {descriptor.focus}",
                5000,
            )


__all__ = ["MainWindow"]
