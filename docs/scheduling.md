# Scheduling & Batch Operations

This guide details how Infra Manager Studio models scheduled tasks, cron tables,
and large batch workflows.

## Cron & Schedule Governance

`SchedulerPanel` renders the list of `CronSchedule` entries from
`ApplicationState`. Each schedule exposes a user-toggleable checkbox that mirrors
whether the job is enabled. Integrate this with fleet cron configs by connecting
the toggle callback to your configuration management layer (e.g. Ansible,
SaltStack, or a bespoke API).

### Adding New Jobs

1. Append a `CronSchedule` dataclass instance with the expression, command, and
   `enabled` flag.
2. Reload the UI or emit a model changed signal to refresh the table.
3. Optionally add annotations (owners, tags) by extending the dataclass and
   adjusting the table columns.

## Batch Waves

`BatchPanel` represents long-running, high-volume maintenance such as access
reviews or container retagging. The panel currently simulates progress with a
`QTimer`, but the structure is ready for integration with queue-based backends.
Update the timer callback to poll job progress from your worker fleet or event
bus.

## Runbooks

`RunbookPanel` acts as a living index of incident and maintenance guides. Pair
runbooks with schedules by referencing them from cron job descriptions or adding
cross-links in automation outputs.
