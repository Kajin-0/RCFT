"""Benchmark source metadata for RCFT classification work."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class BenchmarkSource:
    """Metadata for a literature benchmark source.

    This records what the source should be used for before numerical/theoretical records
    are manually extracted into candidate ledgers.
    """

    key: str
    title: str
    url: str
    category: str
    rank_regime: str
    benchmark_role: str
    extraction_status: str = "not_started"
    notes: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BenchmarkSource":
        return cls(
            key=str(data["key"]),
            title=str(data["title"]),
            url=str(data["url"]),
            category=str(data["category"]),
            rank_regime=str(data["rank_regime"]),
            benchmark_role=str(data["benchmark_role"]),
            extraction_status=str(data.get("extraction_status", "not_started")),
            notes=str(data.get("notes", "")),
            metadata=dict(data.get("metadata", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "key": self.key,
            "title": self.title,
            "url": self.url,
            "category": self.category,
            "rank_regime": self.rank_regime,
            "benchmark_role": self.benchmark_role,
            "extraction_status": self.extraction_status,
            "notes": self.notes,
            "metadata": self.metadata,
        }
