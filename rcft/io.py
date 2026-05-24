"""JSONL input/output utilities for RCFT candidate ledgers."""

from __future__ import annotations

import json
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

from rcft.candidate_schema import Candidate


class CandidateIOError(ValueError):
    """Raised when a candidate ledger cannot be parsed."""


def read_jsonl(path: str | Path) -> Iterator[dict[str, Any]]:
    """Yield raw JSON objects from a JSONL file.

    Blank lines and lines beginning with ``#`` are ignored. Errors include the line
    number so rejected ledgers can be debugged quickly.
    """

    ledger_path = Path(path)
    with ledger_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                obj = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise CandidateIOError(
                    f"invalid JSON in {ledger_path} at line {line_number}: {exc.msg}"
                ) from exc
            if not isinstance(obj, dict):
                raise CandidateIOError(
                    f"expected JSON object in {ledger_path} at line {line_number}, got {type(obj).__name__}"
                )
            yield obj


def read_candidates(path: str | Path) -> Iterator[Candidate]:
    """Yield parsed candidates from a JSONL ledger."""

    for obj in read_jsonl(path):
        yield Candidate.from_dict(obj)


def write_jsonl(records: Iterable[dict[str, Any]], path: str | Path) -> None:
    """Write JSON-serializable records to a JSONL file.

    Parent directories are created automatically.
    """

    ledger_path = Path(path)
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    with ledger_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            handle.write("\n")


def write_candidates(candidates: Iterable[Candidate], path: str | Path) -> None:
    """Write candidates to a JSONL ledger."""

    write_jsonl((candidate.to_dict() for candidate in candidates), path)
