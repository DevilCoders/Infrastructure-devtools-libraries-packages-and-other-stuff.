# Infra Manager Studio

Infra Manager Studio is a PyQt6 based desktop application that brings a
feature rich command center to infrastructure mono-repositories. The
application focuses on GitHub and GitLab automation, CI/CD pipeline
observability, and workflow orchestration within a cohesive hacker-inspired
interface.

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

## Getting Started

```bash
python -m infra_manager.app
```

Add the `--background <path>` argument to apply a custom background image that
fills the window.

The repository ships with a simulated state. Integrations with GitHub and
GitLab can be implemented via the service layer in `infra_manager/services`.

## Packaging with auto-py-to-exe

1. Install the project in a virtual environment with the optional packaging
   tools:

   ```bash
   pip install .[dev]
   ```

2. Launch the auto-py-to-exe interface:

   ```bash
   python -m auto_py_to_exe
   ```

3. Choose `launch_infra_manager.py` as the script to package. This thin wrapper
   guarantees PyInstaller discovers the package resources and entry point.

4. Under *Advanced* > *Additional Hooks*, add `--collect-all infra_manager.ui`
   so the embedded stylesheet is available at runtime.

5. Build the executable. The resulting bundle will render the redesigned neon
   interface and leverage the PyQt6 runtime declared in `pyproject.toml`.

## Documentation

Additional documentation can be found in the [`docs/`](docs) directory:

- [Architecture](docs/architecture.md)
- [Extending the Application](docs/extending.md)
- [Theming Guide](docs/theme.md)
- [Desktop Packaging](docs/packaging.md)
- [Automation & Jobs](docs/automation.md)
- [Scheduling & Batch Operations](docs/scheduling.md)
- [Advanced Feature Catalog](docs/features.md)
- [AI Orchestration & Copilots](docs/ai.md)
- [AI Lab & Training Pipelines](docs/ai_lab.md)
- [Dataset Factory Playbook](docs/datasets.md)
- [Code Lab & Execution Surface](docs/code_lab.md)
