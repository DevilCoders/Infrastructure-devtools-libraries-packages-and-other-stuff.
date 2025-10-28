# Automation & Jobs

Infra Manager Studio consolidates automation, async orchestration, and batch
processing controls into dedicated panels.

## Automation Panel

The **Automation** tab renders records from `ApplicationState.automation_scripts`.
Each record includes the automation name, language, target endpoint, summary,
and a snippet. The default dataset demonstrates:

- A Python bootstrapper for provisioning shared infrastructure.
- A Bash routine for rotating edge certificates.
- A Windows Batch script for patch waves.

Selecting a script populates the read-only viewer, making it easy to copy into
other tooling or editors. Extend the dataclass with parameters or secrets as
needed.

## Async Jobs

The **Async Jobs** tab uses a global `QThreadPool` to simulate asyncio and
multithreaded workloads via `JobRunner`. Replace the mock worker with real
asyncio tasks, Celery jobs, or Temporal workflows. Signals are emitted on
progress and completion, allowing downstream integrations to persist status or
trigger notifications.

## Bulk Operations

The **Bulk Ops** tab mirrors batch processing flows (e.g. repository audits or
entitlement reviews). A `QTimer` drives progress updates and status transitions.
Integrate with queue systems (RabbitMQ, AWS SQS) by hooking `BatchProcess`
records into actual job submissions and updating their progress in response to
backend events.

## Notifications

Automation outcomes can be routed to PagerDuty, Slack, or email by augmenting
the `NotificationPanel` dataset. Connect the notification table to webhooks or
chat bots to alert on job completions or failures.

## AI Driven Automation

Combine the automation stack with the new AI orchestrator:

- Use `AIIntegrationManager.broadcast()` to ask assistants for execution plans
  before triggering pipelines or jobs.
- Persist AI recommendations alongside job results to build a feedback loop for
  future training runs.
- Trigger AI workflows directly from automation outcomes to escalate to
  runbooks, governance reviews, or additional bulk operations.
