"""Application state and data models."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class Repository:
    """Metadata for an infrastructure repository."""

    name: str
    platform: str
    path: Path
    description: str = ""
    tags: List[str] = field(default_factory=list)


@dataclass
class PerformanceMetric:
    """Performance telemetry for infrastructure components."""

    name: str
    value: str
    trend: str
    status: str = "stable"


@dataclass
class Cluster:
    """Managed cluster metadata."""

    name: str
    provider: str
    nodes: int
    version: str
    status: str
    region: str


@dataclass
class VirtualServer:
    """Virtual private server instance metadata."""

    name: str
    provider: str
    cpu: str
    memory: str
    status: str
    location: str


@dataclass
class DeploymentProfile:
    """Local deployment profile settings."""

    name: str
    target: str
    strategy: str
    last_run: str


@dataclass
class ConfigurationTemplate:
    """Advanced configuration templates and presets."""

    name: str
    scope: str
    description: str
    version: str


@dataclass
class ObservabilityProbe:
    """Telemetry feed configuration."""

    name: str
    kind: str
    target: str
    status: str


@dataclass
class SecurityPolicy:
    """Security control and compliance policy metadata."""

    name: str
    coverage: str
    status: str
    last_audit: str


@dataclass
class AutomationScript:
    """Automation script descriptor supporting multiple languages."""

    name: str
    language: str
    target: str
    summary: str
    snippet: str


@dataclass
class CronSchedule:
    """Cron-like scheduled job definition."""

    name: str
    schedule: str
    command: str
    enabled: bool


@dataclass
class AsyncJob:
    """Background asynchronous or multithreaded job definition."""

    name: str
    mode: str
    status: str
    progress: int


@dataclass
class BatchProcess:
    """Bulk/batch processing job metadata."""

    name: str
    items: int
    description: str
    status: str


@dataclass
class NotificationChannel:
    """Notification and ChatOps channel configuration."""

    name: str
    medium: str
    target: str
    status: str


@dataclass
class AccessProfile:
    """Access management profile."""

    name: str
    scope: str
    description: str
    status: str


@dataclass
class Runbook:
    """Operational runbook overview."""

    name: str
    trigger: str
    steps: int
    severity: str


@dataclass
class Blueprint:
    """Infrastructure blueprint definition."""

    name: str
    scope: str
    maturity: str


@dataclass
class DataPipeline:
    """Managed data pipeline metadata."""

    name: str
    schedule: str
    owner: str
    status: str


@dataclass
class ServiceMeshPolicy:
    """Service mesh policy configuration."""

    name: str
    mesh: str
    mode: str
    status: str


@dataclass
class CostStrategy:
    """Cost optimization strategy."""

    name: str
    focus: str
    savings: str


@dataclass
class TenantProfile:
    """Environment or tenant profile."""

    name: str
    environments: List[str]
    owner: str
    health: str


@dataclass
class LoggingSink:
    """Centralized logging sink configuration."""

    name: str
    destination: str
    retention: str
    status: str


@dataclass
class AIModel:
    """Custom model engineered for the internal AI control plane."""

    name: str
    version: str
    modality: str
    status: str
    parameters: str


@dataclass
class AIAssistant:
    """Specialised AI copilot available to infrastructure teams."""

    name: str
    specialization: str
    description: str
    availability: str


@dataclass
class AIWorkflow:
    """Composable AI workflow that automates complex runbooks."""

    name: str
    entrypoint: str
    objective: str
    guardrails: str


@dataclass
class AITrainingRun:
    """Lifecycle metadata for bespoke AI model training."""

    name: str
    dataset: str
    status: str
    metric: str


@dataclass
class AIIntegration:
    """External system bridge powered by the in-house AI orchestrator."""

    name: str
    interface: str
    capability: str
    endpoint: str


@dataclass
class AITrainingProfile:
    """Advanced training configuration covering accelerators and strategies."""

    name: str
    accelerator: str
    parallelism: str
    optimizer: str
    fine_tuning: str
    status: str


@dataclass
class DatasetAsset:
    """Curated production-ready dataset with supported formats and tasks."""

    name: str
    domain: str
    formats: List[str]
    quality: str
    tasks: List[str]


@dataclass
class CodeWorkspace:
    """Executable coding surface embedded inside the operations cockpit."""

    name: str
    language: str
    runner: str
    description: str
    template: str


@dataclass
class AdvancedFeature:
    """High-level advanced feature descriptor for the cockpit."""

    name: str
    category: str
    description: str
    status: str


@dataclass
class InfrastructureTarget:
    """Runtime surface that can be orchestrated from the advanced tab."""

    name: str
    kind: str
    environment: str
    region: str
    status: str
    owner: str
    endpoints: List[str] = field(default_factory=list)
    automation: str = ""
    operations: List[str] = field(default_factory=list)


@dataclass
class ApplicationState:
    """Container for shared application state."""

    repositories: Dict[str, Repository] = field(default_factory=dict)
    workflows: List[str] = field(default_factory=list)
    pipelines: List[str] = field(default_factory=list)
    performance: List[PerformanceMetric] = field(default_factory=list)
    clusters: List[Cluster] = field(default_factory=list)
    servers: List[VirtualServer] = field(default_factory=list)
    deployments: List[DeploymentProfile] = field(default_factory=list)
    configurations: List[ConfigurationTemplate] = field(default_factory=list)
    probes: List[ObservabilityProbe] = field(default_factory=list)
    security_policies: List[SecurityPolicy] = field(default_factory=list)
    automation_scripts: List[AutomationScript] = field(default_factory=list)
    cron_schedules: List[CronSchedule] = field(default_factory=list)
    async_jobs: List[AsyncJob] = field(default_factory=list)
    batch_processes: List[BatchProcess] = field(default_factory=list)
    notification_channels: List[NotificationChannel] = field(default_factory=list)
    access_profiles: List[AccessProfile] = field(default_factory=list)
    runbooks: List[Runbook] = field(default_factory=list)
    blueprints: List[Blueprint] = field(default_factory=list)
    data_pipelines: List[DataPipeline] = field(default_factory=list)
    mesh_policies: List[ServiceMeshPolicy] = field(default_factory=list)
    cost_strategies: List[CostStrategy] = field(default_factory=list)
    tenants: List[TenantProfile] = field(default_factory=list)
    logging_sinks: List[LoggingSink] = field(default_factory=list)
    ai_models: List[AIModel] = field(default_factory=list)
    ai_assistants: List[AIAssistant] = field(default_factory=list)
    ai_workflows: List[AIWorkflow] = field(default_factory=list)
    ai_training_runs: List[AITrainingRun] = field(default_factory=list)
    ai_integrations: List[AIIntegration] = field(default_factory=list)
    ai_training_profiles: List[AITrainingProfile] = field(default_factory=list)
    dataset_assets: List[DatasetAsset] = field(default_factory=list)
    code_workspaces: List[CodeWorkspace] = field(default_factory=list)
    advanced_features: List[AdvancedFeature] = field(default_factory=list)
    infrastructures: List[InfrastructureTarget] = field(default_factory=list)

    @classmethod
    def load(cls) -> "ApplicationState":
        """Load persisted state or create defaults.

        In a real deployment this function would deserialize user preferences
        and repository configuration from disk. Here we provide a set of mock
        values that demonstrate how data flows through the UI.
        """

        state = cls()
        state.repositories = {
            "core-infra": Repository(
                name="core-infra",
                platform="GitHub",
                path=Path("~/workspace/core-infra"),
                description="Mission critical Terraform mono-repo",
                tags=["terraform", "production"],
            ),
            "platform-delivery": Repository(
                name="platform-delivery",
                platform="GitLab",
                path=Path("~/workspace/platform-delivery"),
                description="GitLab CI pipelines for the delivery team",
                tags=["gitlab", "pipelines"],
            ),
        }
        state.workflows = [
            "Apply Terraform plan",
            "Validate Kubernetes manifests",
            "Sync secrets",
        ]
        state.pipelines = [
            "GitHub Actions - Release",
            "GitLab CI - Nightly",
        ]
        state.performance = [
            PerformanceMetric("Terraform Apply", "6m 40s", "-12%", "stable"),
            PerformanceMetric("Kubernetes Deploy", "2m 10s", "+5%", "warning"),
            PerformanceMetric("Ansible Provision", "4m 03s", "-3%", "stable"),
        ]
        state.clusters = [
            Cluster(
                name="prod-eu",
                provider="EKS",
                nodes=42,
                version="1.27",
                status="healthy",
                region="eu-central-1",
            ),
            Cluster(
                name="staging-us",
                provider="GKE",
                nodes=18,
                version="1.26",
                status="scaling",
                region="us-central1",
            ),
        ]
        state.servers = [
            VirtualServer("edge-cache-01", "Hetzner", "8 vCPU", "16 GB", "active", "fsn1"),
            VirtualServer("telemetry-proxy", "Linode", "4 vCPU", "8 GB", "maintenance", "us-east"),
        ]
        state.deployments = [
            DeploymentProfile("Local Docker", "docker-compose", "Rolling", "2024-05-08 11:24"),
            DeploymentProfile("K3s Sandbox", "k3s cluster", "Blue/Green", "2024-05-07 19:02"),
        ]
        state.configurations = [
            ConfigurationTemplate(
                name="Zero Trust Mesh",
                scope="network",
                description="Istio gateway mesh with Consul service discovery integration.",
                version="v2.3",
            ),
            ConfigurationTemplate(
                name="Observability Stack",
                scope="monitoring",
                description="Prometheus, Loki, Tempo with self-healing alerts and SLO dashboards.",
                version="v1.9",
            ),
        ]
        state.probes = [
            ObservabilityProbe("Terraform Lag", "latency", "terraform.apply", "stable"),
            ObservabilityProbe("Cluster Saturation", "capacity", "cluster/prod-eu", "warning"),
            ObservabilityProbe("Log Volume", "ingest", "loki/edge", "stable"),
        ]
        state.security_policies = [
            SecurityPolicy("CIS Benchmark", "linux nodes", "passing", "2024-05-01"),
            SecurityPolicy("Secret Rotation", "vault", "attention", "2024-04-27"),
            SecurityPolicy("Container Signing", "supply chain", "passing", "2024-05-05"),
        ]
        state.automation_scripts = [
            AutomationScript(
                name="Bootstrap Control Plane",
                language="python",
                target="github://core-infra",
                summary="Sets up base networking, IAM, and observability hooks.",
                snippet="""#!/usr/bin/env python3\nprint('Provisioning control plane...')""",
            ),
            AutomationScript(
                name="Rotate Edge Certificates",
                language="bash",
                target="ssh://edge-gateways",
                summary="Bash automation for certificate renewal across edge nodes.",
                snippet="""#!/usr/bin/env bash\nfor host in $EDGE_HOSTS; do echo \"renew $host\"; done""",
            ),
            AutomationScript(
                name="Windows Patch Sweep",
                language="batch",
                target="winrm://ops-segment",
                summary="Batch script rolling out Windows updates to dedicated servers.",
                snippet="""@echo off\necho Starting patch sweep...\nwmic qfe list""",
            ),
        ]
        state.cron_schedules = [
            CronSchedule("Nightly Terraform Plan", "0 2 * * *", "make plan", True),
            CronSchedule("Weekly Cost Snapshot", "0 6 * * MON", "python scripts/cost.py", True),
            CronSchedule("Hourly Log Ship", "0 * * * *", "bash scripts/ship-logs.sh", True),
        ]
        state.async_jobs = [
            AsyncJob("Secrets Sync", "asyncio", "idle", 0),
            AsyncJob("Drift Detector", "multithread", "queued", 0),
            AsyncJob("Metrics Fanout", "asyncio", "idle", 0),
        ]
        state.batch_processes = [
            BatchProcess("Bulk Repo Audit", 24, "Scans repos for policy compliance", "scheduled"),
            BatchProcess("Image Retag", 160, "Retags container images across registries", "ready"),
            BatchProcess("Access Review", 48, "Bulk entitlement review and approvals", "running"),
        ]
        state.notification_channels = [
            NotificationChannel("Incident Pager", "PagerDuty", "SRE Primary", "active"),
            NotificationChannel("Deploy Stream", "Slack", "#deployments", "active"),
            NotificationChannel("Cost Digest", "Email", "finops@company.io", "paused"),
        ]
        state.access_profiles = [
            AccessProfile("Platform Admin", "prod clusters", "Full control of prod clusters", "active"),
            AccessProfile("Read Only", "observability", "Read dashboards and logs", "active"),
            AccessProfile("Pipeline Maintainer", "ci/cd", "Manage pipelines and templates", "review"),
        ]
        state.runbooks = [
            Runbook("Cluster Scale Out", "cpu saturation", 7, "high"),
            Runbook("Secrets Leak", "detected secret", 12, "critical"),
            Runbook("Pipeline Degradation", "latency spike", 6, "medium"),
        ]
        state.blueprints = [
            Blueprint("Multi-Region Active/Active", "resiliency", "beta"),
            Blueprint("Data Lakehouse", "analytics", "stable"),
            Blueprint("Zero Touch Provisioning", "edge", "preview"),
        ]
        state.data_pipelines = [
            DataPipeline("Audit Log ETL", "*/15 * * * *", "security", "healthy"),
            DataPipeline("Cost Metrics", "0 */2 * * *", "finops", "delayed"),
            DataPipeline("KPI Warehouse", "0 1 * * *", "data", "healthy"),
        ]
        state.mesh_policies = [
            ServiceMeshPolicy("Service MTLS", "istio-prod", "strict", "enforced"),
            ServiceMeshPolicy("Traffic Shadow", "linkerd-staging", "shadow", "testing"),
            ServiceMeshPolicy("Rate Limit", "istio-prod", "rate-limit", "enforced"),
        ]
        state.cost_strategies = [
            CostStrategy("Spot Balancer", "compute", "18%"),
            CostStrategy("Storage Tiering", "object storage", "11%"),
            CostStrategy("CI Runner Rightsizing", "pipelines", "7%"),
        ]
        state.tenants = [
            TenantProfile("Payments", ["prod", "staging"], "payments@company.io", "stable"),
            TenantProfile("Analytics", ["prod", "dev"], "data@company.io", "attention"),
            TenantProfile("Internal IT", ["qa", "dev"], "it@company.io", "stable"),
        ]
        state.logging_sinks = [
            LoggingSink("Global Loki", "loki://prod", "30d", "active"),
            LoggingSink("Archive S3", "s3://infra-logs", "180d", "warming"),
            LoggingSink("Security Vault", "elasticsearch://security", "90d", "active"),
        ]
        state.ai_models = [
            AIModel("Sentinel-Deploy", "v0.8.1", "agentic orchestration", "serving", "6.2B params"),
            AIModel("PlanSynth", "v0.6.0", "terraform synthesis", "training", "2.4B params"),
            AIModel("OpsLinguist", "v0.4.3", "runbook reasoning", "serving", "1.1B params"),
        ]
        state.ai_assistants = [
            AIAssistant(
                "Atlas", "infrastructure planning", "Designs rollout blueprints and dependency maps.", "online",
            ),
            AIAssistant(
                "Nyx", "incident response", "Guides responders through mitigation runbooks with context.", "online",
            ),
            AIAssistant(
                "Keeva", "governance", "Reviews policy drift, compliance posture, and audit findings.", "sleeping",
            ),
        ]
        state.ai_workflows = [
            AIWorkflow(
                "Cluster Expansion Advisor",
                "ai.workflows.cluster.scale",
                "Project node requirements and propose placement with cost overlays.",
                "Requires SLO margin above 15% before action",
            ),
            AIWorkflow(
                "Pipeline Optimizer",
                "ai.workflows.pipeline.tune",
                "Simulate stage parallelism and caching strategies for CI pipelines.",
                "Validate compliance checks before enabling parallel builds",
            ),
            AIWorkflow(
                "Secret Hardening",
                "ai.workflows.security.rotate",
                "Automate detection and rotation sequences for leaked secrets.",
                "Escalate to Security if more than 3 rotations within 24h",
            ),
        ]
        state.ai_training_runs = [
            AITrainingRun("Sentinel-Deploy nightly", "deploy_telemetry.parquet", "running", "F1 0.92"),
            AITrainingRun("PlanSynth weekly", "terraform_corpus.jsonl", "queued", "BLEU 0.73"),
            AITrainingRun("OpsLinguist reinforcement", "runbook_dialogs.jsonl", "completed", "ROUGE-L 0.81"),
        ]
        state.ai_integrations = [
            AIIntegration(
                "ChatOps Co-pilot", "webhook", "Summarise incidents and propose responses", "https://ai.local/chatops",
            ),
            AIIntegration(
                "Terraform Drafts", "grpc", "Generate Terraform module diffs on demand", "grpc://ai.local:7447",
            ),
            AIIntegration(
                "CI Advisor", "rest", "Recommend pipeline cache and matrix strategies", "https://ai.local/ci-advice",
            ),
        ]
        state.ai_training_profiles = [
            AITrainingProfile(
                name="Sentinel Parallel Trainer",
                accelerator="GPU",
                parallelism="8-way tensor parallel",
                optimizer="AdamW + gradient checkpointing",
                fine_tuning="LoRA adapters for deployment reasoning",
                status="running",
            ),
            AITrainingProfile(
                name="PlanSynth Hybrid Compiler",
                accelerator="CPU + GPU",
                parallelism="CPU pre-processing with 4 GPU shards",
                optimizer="Hybrid compile then fine-tune",
                fine_tuning="Instruction tuning on IaC diffs",
                status="queued",
            ),
            AITrainingProfile(
                name="OpsLinguist Rapid Tune",
                accelerator="CPU",
                parallelism="Batch synchronous",
                optimizer="Adafactor warm-start",
                fine_tuning="Conversational SRE transcripts",
                status="ready",
            ),
        ]
        state.dataset_assets = [
            DatasetAsset(
                name="Deploy Telemetry Corpus",
                domain="CI/CD automation",
                formats=["jsonl", "parquet", "delta"],
                quality="validated - anomaly filtered",
                tasks=["artifact classification", "failure root-cause", "latency regression"],
            ),
            DatasetAsset(
                name="Runbook Dialogue Studio",
                domain="incident response",
                formats=["yaml", "jsonl"],
                quality="production grade - redacted",
                tasks=["dialogue summarisation", "action extraction", "policy alignment"],
            ),
            DatasetAsset(
                name="Infrastructure Blueprint Library",
                domain="architecture design",
                formats=["markdown", "csv", "graphml"],
                quality="golden paths curated",
                tasks=["pattern synthesis", "compliance tagging", "cost modelling"],
            ),
        ]
        state.code_workspaces = [
            CodeWorkspace(
                name="Terraform Drift Fixer",
                language="python",
                runner="async shell",
                description="Generate terraform patch sets and dry-run via automation APIs.",
                template="""#!/usr/bin/env python3\nasync def main():\n    print('Plan and patch drift...')\n""",
            ),
            CodeWorkspace(
                name="Edge Bootstrap",
                language="bash",
                runner="bash + tmux session",
                description="Provision edge nodes with secure baseline tooling.",
                template="""#!/usr/bin/env bash\nset -euo pipefail\necho 'Patching edge nodes'\n""",
            ),
            CodeWorkspace(
                name="Windows Maintenance",
                language="batch",
                runner="winrm batch executor",
                description="Automate Windows update cadence with logging hooks.",
                template="""@echo off\necho Running maintenance tasks...\n""",
            ),
        ]
        state.advanced_features = [
            AdvancedFeature("Async Job Orchestrator", "Concurrency", "Coordinate asyncio based background workers.", "ready"),
            AdvancedFeature("Multithreaded Pipeline Fanout", "Concurrency", "Distribute CI triggers across thread pools.", "ready"),
            AdvancedFeature("Bulk Repository Sync", "Bulk Ops", "Mirror monorepo modules at scale with retry logic.", "ready"),
            AdvancedFeature("Batch Secret Rotation", "Security", "Rotate thousands of credentials per batch window.", "ready"),
            AdvancedFeature("CronTab Governance", "Scheduling", "Curate fleet cron tables with drift detection.", "ready"),
            AdvancedFeature("Canary Analyzer", "Performance", "Score deployment canaries with custom metrics.", "beta"),
            AdvancedFeature("Service Mesh Policy Builder", "Networking", "Compose mTLS and traffic shaping bundles.", "beta"),
            AdvancedFeature("Observability Autotuner", "Observability", "Auto-tune retention and sampling policies.", "beta"),
            AdvancedFeature("Cost Anomaly Radar", "FinOps", "Detect hourly spend anomalies across tenants.", "beta"),
            AdvancedFeature("Access Drift Monitor", "Security", "Highlight RBAC drift across environments.", "beta"),
            AdvancedFeature("Tenant Isolation Guard", "Governance", "Validate namespace and cluster guardrails.", "beta"),
            AdvancedFeature("Data Pipeline Validator", "Data", "Run schema drift checks for streaming inputs.", "beta"),
            AdvancedFeature("Disaster Recovery Drills", "Resiliency", "Simulate region evacuation runbooks.", "beta"),
            AdvancedFeature("Blue/Green Scoreboard", "Deployments", "Compare live traffic splits in real time.", "beta"),
            AdvancedFeature("ChatOps Responder", "Automation", "Enrich Slack commands with templated flows.", "beta"),
            AdvancedFeature("On-call Rotation Planner", "SRE", "Visualize and optimize on-call coverage.", "beta"),
            AdvancedFeature("Compliance Auditor", "Governance", "Map policies to evidence across repos.", "beta"),
            AdvancedFeature("Security Scan Aggregator", "Security", "Combine SAST, DAST, and IaC scan results.", "beta"),
            AdvancedFeature("Auto-Scaling Tuner", "Performance", "Suggest HPA settings based on telemetry.", "beta"),
            AdvancedFeature("Registry Mirror Manager", "Supply Chain", "Sync container registries with failover.", "beta"),
            AdvancedFeature("Artifact Signer", "Supply Chain", "Sign and verify release artifacts automatically.", "beta"),
            AdvancedFeature("GitOps Sync Controller", "GitOps", "Manage fleet of ArgoCD/Flux controllers.", "beta"),
            AdvancedFeature("Infrastructure Drift Detector", "Governance", "Compare live state vs declarative configs.", "beta"),
            AdvancedFeature("Patch Wave Scheduler", "Maintenance", "Coordinate OS patch waves per compliance.", "beta"),
            AdvancedFeature("SLO Scoreboard", "Reliability", "Track burn rate across services.", "beta"),
            AdvancedFeature("Error Budget Predictor", "Reliability", "Predict burn based on historical incidents.", "beta"),
            AdvancedFeature("Template Library", "Automation", "Share modular Terraform/Helm blueprints.", "beta"),
            AdvancedFeature("Pipeline Analytics", "CI/CD", "Break down pipeline stage duration and success.", "beta"),
            AdvancedFeature("Release Freeze Manager", "Change", "Coordinate change freezes with approvals.", "beta"),
            AdvancedFeature("Multi-cloud Orchestrator", "Cloud", "Deploy workloads across providers with guardrails.", "beta"),
            AdvancedFeature("AI Runbook Partner", "AI", "Pair operators with context-aware assistants per task.", "alpha"),
            AdvancedFeature("Model Observatory", "AI", "Track custom in-house model health and training metrics.", "alpha"),
            AdvancedFeature("AI Workflow Forge", "AI", "Compose guardrailed automation blueprints for AI agents.", "alpha"),
        ]
        state.infrastructures = [
            InfrastructureTarget(
                name="edge-cache-vps",
                kind="vps",
                environment="prod-edge",
                region="eu-central-1",
                status="active",
                owner="edge-platform@company.io",
                endpoints=["https://cache-eu.prod.company.io", "ssh://edge-cache-01"],
                automation="ansible-playbook site.yml -l edge-cache",
                operations=["restart", "snapshot", "scale-out"],
            ),
            InfrastructureTarget(
                name="observability-core",
                kind="container",
                environment="staging",
                region="us-central1",
                status="attention",
                owner="observability@company.io",
                endpoints=["https://grafana.staging.company.io", "grpc://loki-gateway"],
                automation="helm upgrade obs-stack charts/observability",
                operations=["rollout-restart", "run-health-check", "promote"],
            ),
            InfrastructureTarget(
                name="devops-workbench",
                kind="local",
                environment="operators-lab",
                region="on-prem lab",
                status="ready",
                owner="platform-ops@company.io",
                endpoints=["http://localhost:9000", "ssh://lab-gateway"],
                automation="make bootstrap-local",
                operations=["sync-state", "hydrate-secrets", "backup"],
            ),
            InfrastructureTarget(
                name="ml-serving-batch",
                kind="container",
                environment="prod",
                region="asia-southeast1",
                status="healthy",
                owner="ml-platform@company.io",
                endpoints=["https://ml-serving.prod.company.io", "k8s://ml-serving"],
                automation="kubectl rollout restart deployment/ml-serving",
                operations=["rollout-restart", "scale-in", "run-smoke-tests"],
            ),
            InfrastructureTarget(
                name="edge-gateway-vps",
                kind="vps",
                environment="prod-network",
                region="us-east-1",
                status="maintenance",
                owner="networking@company.io",
                endpoints=["ssh://edge-gateway-01", "ssh://edge-gateway-02"],
                automation="ansible-playbook gateway-maintenance.yml",
                operations=["failover", "apply-updates", "restore"],
            ),
            InfrastructureTarget(
                name="lab-sandbox",
                kind="local",
                environment="innovation-lab",
                region="campus west",
                status="provisioning",
                owner="innovation@company.io",
                endpoints=["http://sandbox.lab.local", "vnc://lab-sandbox"],
                automation="./scripts/lab-bootstrap.sh",
                operations=["continue-provision", "reimage", "archive"],
            ),
        ]
        return state


__all__ = [
    "ApplicationState",
    "Repository",
    "PerformanceMetric",
    "Cluster",
    "VirtualServer",
    "DeploymentProfile",
    "ConfigurationTemplate",
    "ObservabilityProbe",
    "SecurityPolicy",
    "AutomationScript",
    "CronSchedule",
    "AsyncJob",
    "BatchProcess",
    "NotificationChannel",
    "AccessProfile",
    "Runbook",
    "Blueprint",
    "DataPipeline",
    "ServiceMeshPolicy",
    "CostStrategy",
    "TenantProfile",
    "LoggingSink",
    "AIModel",
    "AIAssistant",
    "AIWorkflow",
    "AITrainingRun",
    "AIIntegration",
    "AITrainingProfile",
    "DatasetAsset",
    "CodeWorkspace",
    "AdvancedFeature",
    "InfrastructureTarget",
]
