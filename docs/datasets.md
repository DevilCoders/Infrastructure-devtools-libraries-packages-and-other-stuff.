# Dataset Factory Playbook

The dataset factory embedded in Infra Manager Studio helps AI platform teams
package, validate, and distribute corpora tailored to infrastructure tasks.

## Lifecycle Stages

1. **Ingest** – Gather telemetry, runbook transcripts, architecture blueprints,
   and governance evidence from the mono-repositories and observability stack.
2. **Normalize** – Convert inputs into canonical formats (JSONL, Parquet,
   Delta, YAML, Markdown, CSV, GraphML) while preserving schema metadata.
3. **Scrub** – Apply automated PII redaction and anomaly filtering. Record the
   results in `DatasetAsset.quality` to keep audit trails visible.
4. **Augment** – Generate synthetic scenarios for rare incidents or change
   windows. Track augmentation steps in the dataset task list for traceability.
5. **Validate** – Execute schema drift detection and golden-path regression
   tests. The AI Lab checklist in the UI mirrors these validations.
6. **Publish** – Emit dataset manifests to the model registry and document the
   tasks, owners, and release cadence.

## Multi-format Support

The application surfaces every supported format so that downstream tools can
choose the most efficient representation. You can extend the list inside
`ApplicationState.load()` or add custom conversion jobs via the Automation tab.

## Governance Hooks

- Link dataset refreshes to cron schedules for predictable curation.
- Use notification channels to broadcast release notes to AI consumers.
- Combine the AI Lab view with the AI Training tab to confirm that fine-tunes
  only consume certified datasets.

Following this playbook ensures that datasets powering your custom AI remain
production-ready, well-documented, and compliant with organisational guardrails.
