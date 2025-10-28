# AI Orchestration & Copilot Guide

Infra Manager Studio ships with a ground-up AI orchestration layer designed to
augment infrastructure engineers without relying on external SaaS providers.
This document outlines the major components, how the UI surfaces them, and how
you can extend the stack.

## Components

- **Custom models** – `AIModel` entries in `core/state.py` describe the in-house
  models powering the assistants. Each model tracks modality, lifecycle stage,
  and parameter counts.
- **Assistants** – `AIAssistant` records define the personas exposed in the **AI
  Assistants** tab. Each assistant specialises on a platform concern (planning,
  incident response, governance) and can be wired into chat or automation
  workflows.
- **Workflows** – `AIWorkflow` entries map orchestration entrypoints to
  objectives with guardrails. The **AI Workflows** tab illustrates how these
  guardrails are communicated before execution.
- **Training runs** – `AITrainingRun` data highlights model evolution,
  referencing datasets, lifecycle status, and key metrics.
- **Integrations** – `AIIntegration` definitions connect the orchestrator to
  Slack, Git providers, CI/CD, and other internal endpoints for closed-loop
  automation.

## AI Lab

The **AI Lab** tab expands on traditional training views with rich
`AITrainingProfile` and `DatasetAsset` models. Profiles capture accelerator
mixes (CPU, GPU, or hybrid), parallelism settings, optimizers, and fine-tuning
strategies so operators can reason about multi-stage runs at a glance. Dataset
entries catalogue every production task, supported format (JSONL, Parquet,
Delta, YAML, Markdown, CSV, GraphML, and more), and quality gate status to keep
curation efforts auditable.

Use the lab to walk through the dataset checklist, coordinate LoRA or
instruction-tuning sessions, and validate that synthetic augmentations and PII
scrubbing completed before scheduling jobs through the automation or cron
panels.

## Services

`services/ai.py` exposes a protocol-first interface for the orchestrator. The
`AIOrchestratorClient` protocol describes the runtime surface and ships with a
`LocalAIOrchestrator` demo implementation. `AIIntegrationManager` coordinates
broadcasting instructions to the orchestrator and collecting responses. Replace
these implementations with production clients to talk to your real AI control
plane.

## Extending

1. Add new assistants or models to `ApplicationState.load()` to surface them in
   the UI immediately.
2. Implement the `AIOrchestratorClient` protocol to connect to your inference or
   planning backend.
3. Register automation hooks (cron jobs, async jobs, or batch processes) that
   invoke the orchestrator for autonomous operations.
4. Document new workflows under `docs/ai.md` so contributors understand the
   expected guardrails and escalation paths.

By keeping the AI surface grounded in local data models and protocols, the
studio enables rich copilots while retaining full control over governance,
privacy, and deployment strategy.
