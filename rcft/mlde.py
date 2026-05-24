"""MLDE search scaffolding.

This module is a placeholder for modular-linear-differential-equation generation.
The verifier layer should remain independent of any one generator so that MLDE,
VVMF, known-theory, and AI-proposed candidates all pass through the same checks.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class MLDEScanConfig:
    n_characters: int
    central_charge_min: Fraction
    central_charge_max: Fraction
    max_denominator: int
    q_precision: int
    wronskian_index: int | None = None


def validate_mlde_scan_config(config: MLDEScanConfig) -> None:
    if config.n_characters < 1:
        raise ValueError("n_characters must be positive")
    if config.central_charge_min > config.central_charge_max:
        raise ValueError("central_charge_min must be <= central_charge_max")
    if config.max_denominator < 1:
        raise ValueError("max_denominator must be positive")
    if config.q_precision < 1:
        raise ValueError("q_precision must be positive")
