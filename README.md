# Infra Manager Studio

Infra Manager Studio is a PyQt6 based desktop application that brings a
feature rich command center to infrastructure mono-repositories. The
application focuses on GitHub and GitLab automation, CI/CD pipeline
observability, and workflow orchestration within a cohesive hacker-inspired
interface. The latest release expands the cockpit with dozens of specialist
modules, dynamically generated command center tabs, and a reusable capability
panel that keeps critical telemetry, highlights, and automation hooks at your
fingertips.

## Highlights

- **Dark neon aesthetics** – black and blood red accents with subtle
  animations and frosted glass components.
- **Repository intelligence** – curated views of mono-repositories and
  metadata to help platform and infrastructure teams move fast.
- **Pipeline control** – trigger and observe CI/CD pipelines across GitHub
  Actions and GitLab CI with a consistent abstraction layer.
- **Workflow requests** – capture custom workflow runs with context before
  dispatching to automation backends.
- **Operations cockpit** – dedicated tabs for performance telemetry, cluster
  capacity, VPS lifecycle actions, local deployment profiles, and advanced
  configuration templates.
- **Advanced control plane** – more than thirty expert features spanning async
  orchestration, governance, multi-cloud, and finops insights in new tabs.
- **Automation studio** – launch Python, Bash, and Batch automations, govern
  cron schedules, and monitor async/multithreaded execution side-by-side.
- **AI copilots** – orchestrate bespoke assistants, models, workflows, and
  integrations purpose-built for infrastructure teams.
- **AI laboratory** – tune CPU, GPU, and hybrid training waves with dataset
  governance workflows in the new AI Lab tab.
- **Code lab** – draft Python, Bash, and Batch automations with inline run
  previews before promoting to production pipelines.
- **Modular architecture** – UI, service layer, and state management are
  decoupled for easy extension.
- **Command center carousel** – fifty three command center descriptors drive
  dynamic tab creation, each surfacing a dedicated capability panel with
  status-bar aware focus cues and task automation shortcuts.
- **Capability panel widgets** – shareable UI components present highlights,
  metrics, and quick actions for every module, keeping workflows consistent as
  you jump between features.

## Getting Started

```bash
python -m infra_manager.app
```

Add the `--background <path>` argument to apply a custom background image that
fills the window.

The repository ships with a simulated state. Integrations with GitHub and
GitLab can be implemented via the service layer in `infra_manager/services`.

### Exploring the expanded cockpit

After launching the application you will see the Operations Cockpit stocked
with more than fifty infrastructure modules and capability tabs. Each tab is
generated from the seeded command center descriptors and renders a capability
panel that highlights the module focus, recommended automations, and telemetry
callouts. Switching between tabs updates the status bar with contextual
insights so you can keep track of the active surface while navigating the
expanded inventory.

The Codebase Manager panel continues to provide a rich blend of module
exploration, configuration forms, and profile matching tables so you can manage
mono-repository automation side-by-side with the new cockpit experiences.

## Documentation

Additional documentation can be found in the [`docs/`](docs) directory:

- [Architecture](docs/architecture.md)
- [Extending the Application](docs/extending.md)
- [Theming Guide](docs/theme.md)
- [Automation & Jobs](docs/automation.md)
- [Scheduling & Batch Operations](docs/scheduling.md)
- [Advanced Feature Catalog](docs/features.md)
- [AI Orchestration & Copilots](docs/ai.md)
- [AI Lab & Training Pipelines](docs/ai_lab.md)
- [Dataset Factory Playbook](docs/datasets.md)
- [Code Lab & Execution Surface](docs/code_lab.md)
