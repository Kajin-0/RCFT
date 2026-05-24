"""Modular data placeholders and exact T-phase helpers.

This module intentionally starts small. Later milestones should add exact cyclotomic
representations for S and T matrices rather than using floating-point complex numbers.
"""

from __future__ import annotations

from fractions import Fraction

from rcft.candidate_schema import Character


def t_phase_exponent(character: Character) -> Fraction:
    """Return the rational exponent h - c/24 defining T_ii = exp(2*pi*i*exponent)."""

    return character.leading_exponent


def reduce_mod_one(value: Fraction) -> Fraction:
    """Reduce an exact rational modulo 1 into [0, 1)."""

    numerator = value.numerator % value.denominator
    return Fraction(numerator, value.denominator)


def t_phase_exponents_mod_one(characters: tuple[Character, ...]) -> tuple[Fraction, ...]:
    """Return exact T-phase exponents reduced modulo 1."""

    return tuple(reduce_mod_one(t_phase_exponent(character)) for character in characters)
