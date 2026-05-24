"""Vector-valued modular-form search scaffolding.

The VVMF route is expected to become the main path for rank four to six searches.
For now, this module only defines explicit configuration objects and validation.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VVMFScanConfig:
    representation_label: str
    weight_min: int
    weight_max: int
    q_precision: int
    coefficient_bound: int


def validate_vvmf_scan_config(config: VVMFScanConfig) -> None:
    if not config.representation_label:
        raise ValueError("representation_label must be nonempty")
    if config.weight_min > config.weight_max:
        raise ValueError("weight_min must be <= weight_max")
    if config.q_precision < 1:
        raise ValueError("q_precision must be positive")
    if config.coefficient_bound < 1:
        raise ValueError("coefficient_bound must be positive")
