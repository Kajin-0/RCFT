"""Exact-arithmetic helpers.

The project intentionally stores rational quantities as strings at the data boundary.
Internally, Python's Fraction is used for the initial verifier layer. SageMath can be
introduced behind this interface for deeper modular-form work.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


def parse_fraction(value: str | int | Fraction) -> Fraction:
    """Parse an exact rational value.

    Accepted examples: ``"0"``, ``"1/3"``, ``"-47/48"``, ``2``, ``Fraction(1, 2)``.
    Decimal strings are deliberately rejected because this codebase should not silently
    introduce floating-point approximations into RCFT candidate records.
    """

    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value, 1)
    if not isinstance(value, str):
        raise TypeError(f"Expected str, int, or Fraction, got {type(value)!r}")
    if "." in value:
        raise ValueError(f"Decimal rational input is not allowed: {value!r}")
    return Fraction(value)


def parse_fraction_list(values: Iterable[str | int | Fraction]) -> tuple[Fraction, ...]:
    """Parse an iterable of exact rational values into an immutable tuple."""

    return tuple(parse_fraction(value) for value in values)


def is_integer(value: Fraction) -> bool:
    """Return True if an exact rational has denominator one."""

    return value.denominator == 1
