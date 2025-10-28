# Architecture Overview

Infra Manager Studio follows a layered architecture to separate concerns and
simplify extension.

## Layout

```
src/
└── infra_manager/
    ├── app.py                # Application entry point and bootstrapping
    ├── core/                 # State management and domain models
    ├── services/             # External integrations (GitHub, GitLab, etc.)
    └── ui/                   # UI components built with PyQt6
        ├── main_window.py    # Top level window composition
        ├── theme.py          # Styling primitives and palette helpers
        └── widgets/          # Reusable widgets and panels
```

Each layer communicates with the one below it using simple data objects and
protocols. UI widgets emit signals that can be connected to concrete service
implementations without requiring UI modifications.

## Application State

`core/state.py` defines the `ApplicationState` container plus domain models for
repositories, performance telemetry, clusters, VPS nodes, deployment profiles,
configuration templates, observability probes, security policies, automation
scripts, cron schedules, async jobs, batch processes, notification channels,
access profiles, runbooks, blueprints, data pipelines, service mesh policies,
FinOps strategies, tenant profiles, logging sinks, custom AI models,
assistants, workflows, training runs, integrations, AI training profiles,
dataset assets, embedded code workspaces, and the 30+ advanced feature catalog.
The application is bootstrapped with demo data to showcase
functionality without live services. Persisting the state can be implemented by
serializing `ApplicationState` to a preferred format (e.g. TOML or JSON) during
shutdown.

## Service Layer

`services/automation.py` contains protocols for CI/CD integrations. Implement
`PipelineClient` for GitHub, GitLab, Jenkins or any other provider and inject it
where the UI listens for pipeline triggers. `services/ai.py` houses the bespoke
AI orchestrator protocol and reference client used by the AI panels to reason
about automation plans, produce recommendations, and coordinate multi-channel
integrations.

## UI Composition

The UI is driven by Qt's signal/slot mechanism:

- `RepositoryPanel` emits `repositorySelected` when the user highlights a repo.
- `PipelinePanel` emits `pipelineTriggered` with the selected pipeline name.
- `WorkflowPanel` emits `workflowRequested` with contextual notes.
- `VPSPanel` emits `serverActionRequested` with the desired operation and
  target instance identifier.
- `DeploymentPanel` emits `deploymentRequested` with the selected profile
  object for local rollouts.
- `ConfigurationPanel` emits `templateSelected` for advanced configuration
  editing and export flows.
- `SchedulerPanel` surfaces enable/disable hooks for cron expressions.
- `AsyncJobsPanel` uses a Qt thread pool to execute background job simulations.
- `BatchPanel` mimics wave-based batch execution with progress updates.
- `AutomationPanel` exposes Python, Bash, and Batch snippets for reuse.
- `AdvancedFeaturePanel` and the surrounding operations panels (observability,
  security, notifications, access, runbooks, blueprints, data pipelines,
  service mesh, cost, tenants, logging) provide curated overviews for 30 new
  feature areas without additional wiring requirements. Newly added AI panels
  (assistants, models, workflows, training, integrations, and the AI Lab) expose
  the custom AI control plane directly in the cockpit.
- `CodeLabPanel` delivers an inline editor and execution log so operators can
  iterate on infrastructure automations before dispatching them via other tabs.

`MainWindow` reacts to these signals and updates the status bar. Hooking these
signals to automation clients enables full round-trip automation.
