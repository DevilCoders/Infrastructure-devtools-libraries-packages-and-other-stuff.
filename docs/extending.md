# Extending Infra Manager Studio

This guide outlines patterns for adding functionality without compromising the
architecture or aesthetics.

## Add a New Automation Provider

1. Create a class implementing `PipelineClient` in `infra_manager/services`.
2. Connect the implementation to the `pipelineTriggered` signal from
   `PipelinePanel`.
3. Display execution updates in `PipelinePanel.log_view` or route them to a
   dedicated monitoring widget.

## Integrate Infrastructure as Code Tools

- Extend `ApplicationState.repositories` with metadata such as Terraform
  workspaces or Pulumi stacks.
- Augment `RepositoryPanel` to show environment specific icons or badges.
- Use Qt's model/view architecture for large sets of modules.

## Expand Operations Dashboards

- Populate `ApplicationState.performance`, `clusters`, and `servers` with live
  telemetry. Adapt `PerformancePanel` or `ClusterPanel` to consume streaming
  updates via websockets or message queues.
- Connect `VPSPanel.serverActionRequested` to orchestration APIs (e.g. Ansible,
  Packer, custom Terraform runners) to execute lifecycle operations.
- Extend `DeploymentPanel` with pipeline stage breakdowns or integrate dev
  containers by adding new properties to `DeploymentProfile`.
- Persist curated blueprints by writing selected `ConfigurationTemplate`
  objects to disk or a configuration service.
- Populate the new observability, security, access, notification, cost, mesh,
  and tenant panels by wiring their data classes to live systems (e.g. Prometheus,
  Vault, Okta, PagerDuty, or cost explorers).
- Expand the advanced feature catalog by appending new `AdvancedFeature`
  descriptors and pointing their descriptions to your implementation docs.

## AI Orchestration

- Add custom AI models, assistants, workflows, training runs, or integrations to
  `ApplicationState.load()` so they appear in the dedicated AI tabs.
- Implement the `AIOrchestratorClient` protocol from `services/ai.py` to connect
  to a production inference layer or planning service.
- Use `AIIntegrationManager.broadcast()` to coordinate calls between multiple
  AI endpoints (e.g. ChatOps, Git, CI). Wire responses back into automation or
  notification panels for follow-up actions.
- Capture audit trails or usage statistics by persisting `AIResponse` data
  alongside runbook or incident records.

## Async, Batch, and Scheduling Extensions

- Implement real async workloads by replacing `JobRunner` with tasks scheduled
  via `asyncio` or integrating `concurrent.futures` executors.
- Persist job history by storing `AsyncJob` and `BatchProcess` progress in a
  queue or database and refreshing the panels on completion signals.
- Bind `SchedulerPanel` toggles to a cron-as-a-service backend or configuration
  management system to apply changes automatically.

## Automation and Scripting Enhancements

- Add script records to `ApplicationState.automation_scripts` with Python,
  Bash, Batch, PowerShell, or other interpreters as needed.
- Use the selected snippet from `AutomationPanel` to seed editors or dispatch
  scripts to a remote runner via SSH/WinRM.
- Extend automation metadata with parameter schemas by introducing additional
  dataclass fields and updating the panel to render forms dynamically.

## Workflow Automation

1. Add new workflow definitions to `ApplicationState.workflows` or load them
   dynamically from disk.
2. Customize `WorkflowPanel` to capture additional parameters using `QFormLayout`
   inputs.
3. Route the `workflowRequested` signal to automation services that perform the
   desired tasks (e.g. Argo Workflows, Temporal, Jenkins).

## Visual Customization

- Update colors and fonts in `Theme.default()`.
- Provide additional theme variants and expose them in the toolbar for quick
  switching.
- Store user selected background images in a configuration file and restore them
  on launch by extending `ApplicationState` persistence.

## Packaging and Distribution

- Use `fbs`, `PyInstaller`, or `Briefcase` to generate platform-specific
  installers.
- Include `PySide6` in the build requirements and set the entry point to
  `infra_manager.app:main`.

## Testing Strategy

- Test service layer logic with pytest by mocking external APIs.
- Use Qt's `QTest` module or `pytest-qt` for widget level testing.
- Keep UI logic in small widgets to make testing easier.
- Add contract tests ensuring panel signals translate to the correct backend
  operations when integrating orchestration providers.
