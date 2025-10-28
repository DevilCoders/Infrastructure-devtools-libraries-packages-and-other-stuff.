"""Service layer abstractions for CI/CD automation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class PipelineRequest:
    repository: str
    pipeline: str
    parameters: dict[str, str]


class PipelineClient(Protocol):
    """Protocol for pipeline service clients."""

    def trigger(self, request: PipelineRequest) -> str:
        """Trigger a pipeline and return a reference to the execution."""


class GitHubActionsClient:
    """Example client implementation."""

    def trigger(self, request: PipelineRequest) -> str:
        return f"gh-actions://{request.repository}/{request.pipeline}"


class GitLabCIClient:
    """Example client implementation."""

    def trigger(self, request: PipelineRequest) -> str:
        return f"gitlab-ci://{request.repository}/{request.pipeline}"


__all__ = ["PipelineRequest", "PipelineClient", "GitHubActionsClient", "GitLabCIClient"]
