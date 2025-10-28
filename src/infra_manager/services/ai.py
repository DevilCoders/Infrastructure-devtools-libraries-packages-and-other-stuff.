"""Custom AI orchestrator integration points."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Protocol


@dataclass
class AIInstruction:
    """Instruction payload sent to the orchestrator."""

    assistant: str
    objective: str
    context: dict[str, str]


@dataclass
class AIResponse:
    """Structured response emitted by the orchestrator."""

    summary: str
    follow_up: list[str]
    confidence: float


class AIOrchestratorClient(Protocol):
    """Protocol describing the in-house AI orchestrator surface."""

    def execute(self, instruction: AIInstruction) -> AIResponse:
        """Submit an instruction and return a structured response."""


class LocalAIOrchestrator:
    """Reference implementation used for demos and tests."""

    def execute(self, instruction: AIInstruction) -> AIResponse:  # pragma: no cover - demo stub
        context_summary = ", ".join(f"{k}={v}" for k, v in instruction.context.items())
        summary = (
            f"[{instruction.assistant}] {instruction.objective} — "
            f"context: {context_summary or 'none'}"
        )
        follow_up = [
            "Validate with automation dry-run",
            "Capture results in runbook",
        ]
        return AIResponse(summary=summary, follow_up=follow_up, confidence=0.76)


class AIIntegrationManager:
    """High-level helper that coordinates multi-endpoint AI integrations."""

    def __init__(self, client: AIOrchestratorClient) -> None:
        self._client = client

    def broadcast(self, instructions: Iterable[AIInstruction]) -> list[AIResponse]:
        """Execute a series of instructions and collect responses."""

        return [self._client.execute(instruction) for instruction in instructions]


__all__ = [
    "AIInstruction",
    "AIResponse",
    "AIOrchestratorClient",
    "LocalAIOrchestrator",
    "AIIntegrationManager",
]
