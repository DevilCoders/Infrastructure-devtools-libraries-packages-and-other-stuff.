# Code Lab & Execution Surface

The Code Lab tab introduces an embedded workspace for iterating on automation
snippets without switching tools.

## Workspaces

Each `CodeWorkspace` entry bundles a language, runner, description, and starter
snippet. Infra Manager ships with Python, Bash, and Batch templates:

- **Terraform Drift Fixer** – Python async utility that stages patch sets and
  previews plans.
- **Edge Bootstrap** – Hardened Bash bootstrapper for edge nodes.
- **Windows Maintenance** – Batch script orchestrating update waves via WinRM.

Selecting a workspace updates the editor with the relevant template and displays
metadata about the execution backend.

## Editing & Execution

- The code editor uses a monospace layout with tab stops tuned for infrastructure
  scripting.
- "Run Workspace" simulates execution by emitting a console log showing the
  selected runner, language, and a preview of the script.
- Use the console output to confirm environment selection before handing the
  snippet to the Automation, Async Jobs, or Batch tabs for real execution.

## Extensibility

Add new workspaces by extending the `code_workspaces` list in
`ApplicationState.load()`. Provide custom runners (e.g., Kubernetes Jobs,
Nomad task drivers, GitHub Actions) and snippets pointing to your internal
playbooks.

Because the Code Lab uses the same neon-dark theming as the rest of the app, it
feels cohesive while offering a dedicated zone for code ideation and testing.
