"""Minimal q-series helpers for truncated character data."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable

from rcft.exact import parse_fraction_list


def truncate(coefficients: Iterable[Fraction], precision: int) -> tuple[Fraction, ...]:
    """Return the first ``precision`` coefficients."""

    if precision < 0:
        raise ValueError("precision must be nonnegative")
    return tuple(coefficients)[:precision]


def coefficient_vector(values: Iterable[str | int | Fraction]) -> tuple[Fraction, ...]:
    """Parse coefficient data as exact rationals."""

    return parse_fraction_list(values)


def add_series(a: Iterable[Fraction], b: Iterable[Fraction], precision: int) -> tuple[Fraction, ...]:
    """Add two truncated q-series coefficient vectors."""

    a_tuple = truncate(a, precision)
    b_tuple = truncate(b, precision)
    return tuple(
        (a_tuple[i] if i < len(a_tuple) else Fraction(0))
        + (b_tuple[i] if i < len(b_tuple) else Fraction(0))
        for i in range(precision)
    )


def multiply_series(a: Iterable[Fraction], b: Iterable[Fraction], precision: int) -> tuple[Fraction, ...]:
    """Multiply two truncated q-series coefficient vectors."""

    if precision < 0:
        raise ValueError("precision must be nonnegative")
    a_tuple = truncate(a, precision)
    b_tuple = truncate(b, precision)
    out = [Fraction(0) for _ in range(precision)]
    for i, ai in enumerate(a_tuple):
        for j, bj in enumerate(b_tuple):
            k = i + j
            if k >= precision:
                break
            out[k] += ai * bj
    return tuple(out)
