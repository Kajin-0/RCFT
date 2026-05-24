"""Deterministic content hashing for candidate ledgers."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from rcft.candidate_schema import Candidate


def canonical_json(data: dict[str, Any]) -> str:
    """Return canonical compact JSON for hashing."""

    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(data: dict[str, Any]) -> str:
    """Return SHA-256 hash of canonical JSON."""

    return hashlib.sha256(canonical_json(data).encode("utf-8")).hexdigest()


def candidate_hash(candidate: Candidate) -> str:
    """Hash a candidate's canonical dictionary representation."""

    return sha256_json(candidate.to_dict())
