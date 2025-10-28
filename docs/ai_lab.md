# AI Lab & Training Pipelines

The AI Lab tab gives platform engineers a dedicated space to orchestrate
advanced AI training programs without leaving the Infra Manager cockpit.

## Training Profiles

`AITrainingProfile` records capture the accelerator mix (CPU, GPU, or hybrid),
parallelism topology, optimizer stack, and fine-tuning scope for each training
wave. Use these entries to reason about:

- Warmup phases that rely on CPU preprocessing before GPU shards take over.
- Distributed tensor parallel or pipeline parallel plans across data centers.
- Fine-tuning modes such as LoRA, instruction tuning, or reinforcement
  top-ups tailored to infrastructure tasks.

Selecting a profile in the UI surfaces its current status, making it easy to
trace which runs are actively training, queued, or ready for launch.

## Dataset Factory

`DatasetAsset` entries represent production-ready corpora with multi-format
support. Each asset tracks:

- Domains (CI/CD automation, incident response, architecture design, and more).
- Accepted formats ranging from JSONL and Parquet to YAML, Markdown, CSV, and
  GraphML.
- Quality gates such as anomaly filtering, redaction, or curated golden paths.
- Downstream tasks including classification, summarisation, pattern synthesis,
  and cost modelling.

The panel includes a checklist covering schema validation, PII scrubbing,
synthetic augmentation, and manifest publication to help teams certify data
before triggering large-scale training jobs.

## Workflow Integration

Once profiles and datasets are ready, operators can:

1. Schedule recurring fine-tunes via the Cron & Schedules tab.
2. Dispatch ad-hoc bursts from the Automation tab using Python, Bash, or Batch
   scripts.
3. Review resulting metrics in the AI Training tab, and roll the models into the
   AI Assistants or Integrations surfaces.

The AI Lab keeps the full lifecycle—from dataset curation to parallel training
configuration—visible inside a single neon-dark workspace.
