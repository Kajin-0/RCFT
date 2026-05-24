"""Data schema for rational conformal field theory candidates."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from typing import Any

from rcft.exact import parse_fraction, parse_fraction_list


class CertificateStage(str, Enum):
    """Staged certification ladder for RCFT candidate records.

    The stage names deliberately distinguish admissible q-series from realized RCFTs.
    """

    GENERATED = "generated"
    SCHEMA_VALID = "schema_valid"
    ADMISSIBLE_Q_SERIES = "admissible_q_series"
    MODULAR_DATA_RECOVERED = "modular_data_recovered"
    VERLINDE_PASSING = "verlinde_passing"
    TENABLE = "tenable"
    MATCHED_KNOWN = "matched_known"
    UNRESOLVED_CANDIDATE = "unresolved_candidate"
    REJECTED = "rejected"


@dataclass(frozen=True)
class GeneratorProvenance:
    """Information about how a candidate was generated."""

    method: str = "unknown"
    reference_key: str | None = None
    parameters: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "GeneratorProvenance":
        if data is None:
            return cls()
        return cls(
            method=str(data.get("method", "unknown")),
            reference_key=None if data.get("reference_key") is None else str(data["reference_key"]),
            parameters=dict(data.get("parameters", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "method": self.method,
            "reference_key": self.reference_key,
            "parameters": self.parameters,
        }


@dataclass(frozen=True)
class Character:
    """Truncated RCFT character data.

    The character is represented as

        chi(q) = q^(h - c/24) * sum_m a_m q^m.

    Only the coefficient sequence is stored here. The leading exponent is derived from
    the conformal weight h and central charge c.
    """

    label: str
    h: Fraction
    c: Fraction
    coefficients: tuple[Fraction, ...]

    @property
    def leading_exponent(self) -> Fraction:
        return self.h - self.c / 24

    @classmethod
    def from_dict(cls, data: dict[str, Any], *, central_charge: Fraction) -> "Character":
        return cls(
            label=str(data.get("label", "sector")),
            h=parse_fraction(data["h"]),
            c=central_charge,
            coefficients=parse_fraction_list(data.get("coefficients", [])),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "h": str(self.h),
            "leading_exponent": str(self.leading_exponent),
            "coefficients": [str(value) for value in self.coefficients],
        }


@dataclass(frozen=True)
class Candidate:
    """Machine-checkable candidate character vector."""

    candidate_id: str
    source: str
    n_characters: int
    central_charge: Fraction
    characters: tuple[Character, ...]
    q_precision: int
    wronskian_index: int | None = None
    certificate_stage: CertificateStage = CertificateStage.GENERATED
    subgroup: str = "SL2Z"
    provenance: GeneratorProvenance = field(default_factory=GeneratorProvenance)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Candidate":
        c = parse_fraction(data["central_charge"])
        chars = tuple(Character.from_dict(item, central_charge=c) for item in data["characters"])
        n_characters = int(data.get("n_characters", len(chars)))
        return cls(
            candidate_id=str(data["candidate_id"]),
            source=str(data.get("source", "unknown")),
            n_characters=n_characters,
            central_charge=c,
            characters=chars,
            q_precision=int(data.get("q_precision", min((len(ch.coefficients) for ch in chars), default=0))),
            wronskian_index=(
                None if data.get("wronskian_index") is None else int(data["wronskian_index"])
            ),
            certificate_stage=CertificateStage(data.get("certificate_stage", CertificateStage.GENERATED.value)),
            subgroup=str(data.get("subgroup", "SL2Z")),
            provenance=GeneratorProvenance.from_dict(data.get("provenance")),
            metadata=dict(data.get("metadata", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "source": self.source,
            "n_characters": self.n_characters,
            "central_charge": str(self.central_charge),
            "wronskian_index": self.wronskian_index,
            "q_precision": self.q_precision,
            "certificate_stage": self.certificate_stage.value,
            "subgroup": self.subgroup,
            "provenance": self.provenance.to_dict(),
            "characters": [character.to_dict() for character in self.characters],
            "metadata": self.metadata,
        }
