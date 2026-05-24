"""Exact affine Lie algebra helper formulas for WZW benchmark targets."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from rcft.exact import parse_fraction


@dataclass(frozen=True)
class AffineTheoryData:
    """Minimal exact data for an affine WZW benchmark theory.

    The formulas used are

        c = k * dim(g) / (k + h_dual)
        h_lambda = C2(lambda) / (k + h_dual)

    where ``h_dual`` is the dual Coxeter number and ``C2(lambda)`` is the
    quadratic Casimir eigenvalue of the finite-dimensional highest-weight
    representation in the normalization used by the WZW model.
    """

    algebra: str
    level: int
    dimension_lie_algebra: int
    dual_coxeter_number: int
    nonvacuum_representation: str
    nonvacuum_representation_dimension: int
    nonvacuum_quadratic_casimir: Fraction

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AffineTheoryData":
        return cls(
            algebra=str(data["algebra"]),
            level=int(data["level"]),
            dimension_lie_algebra=int(data["dimension_lie_algebra"]),
            dual_coxeter_number=int(data["dual_coxeter_number"]),
            nonvacuum_representation=str(data["nonvacuum_representation"]),
            nonvacuum_representation_dimension=int(data["nonvacuum_representation_dimension"]),
            nonvacuum_quadratic_casimir=parse_fraction(data["nonvacuum_quadratic_casimir"]),
        )

    @property
    def denominator(self) -> int:
        return self.level + self.dual_coxeter_number

    @property
    def central_charge(self) -> Fraction:
        return Fraction(self.level * self.dimension_lie_algebra, self.denominator)

    @property
    def nonvacuum_conformal_weight(self) -> Fraction:
        return self.nonvacuum_quadratic_casimir / self.denominator

    def to_candidate_metadata(self) -> dict[str, object]:
        return {
            "algebra": self.algebra,
            "level": self.level,
            "dimension_lie_algebra": self.dimension_lie_algebra,
            "dual_coxeter_number": self.dual_coxeter_number,
            "nonvacuum_representation": self.nonvacuum_representation,
            "nonvacuum_representation_dimension": self.nonvacuum_representation_dimension,
            "nonvacuum_quadratic_casimir": str(self.nonvacuum_quadratic_casimir),
            "wzw_denominator": self.denominator,
            "central_charge": str(self.central_charge),
            "nonvacuum_conformal_weight": str(self.nonvacuum_conformal_weight),
        }
