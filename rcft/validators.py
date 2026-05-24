"""Verifier-first validation utilities for RCFT candidate records."""

from __future__ import annotations

from dataclasses import dataclass, field

from rcft.candidate_schema import Candidate, Character
from rcft.exact import is_integer


@dataclass(frozen=True)
class ValidationResult:
    """Structured validation result.

    A failed result contains machine-readable error labels. These labels are intended
    to become the rejection taxonomy used by later AI-guided searches.
    """

    passed: bool
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    details: dict[str, object] = field(default_factory=dict)


def has_integral_coefficients(character: Character) -> bool:
    return all(is_integer(value) for value in character.coefficients)


def has_nonnegative_coefficients(character: Character) -> bool:
    return all(value >= 0 for value in character.coefficients)


def is_vacuum_character(character: Character) -> bool:
    return character.h == 0 and bool(character.coefficients) and character.coefficients[0] == 1


def first_nonintegral_depth(character: Character) -> int | None:
    for index, value in enumerate(character.coefficients):
        if not is_integer(value):
            return index
    return None


def first_negative_depth(character: Character) -> int | None:
    for index, value in enumerate(character.coefficients):
        if value < 0:
            return index
    return None


def validate_candidate(candidate: Candidate) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, object] = {}

    if candidate.n_characters != len(candidate.characters):
        errors.append("n_character_mismatch")
        details["declared_n_characters"] = candidate.n_characters
        details["actual_n_characters"] = len(candidate.characters)

    vacuum_count = sum(is_vacuum_character(character) for character in candidate.characters)
    details["vacuum_count"] = vacuum_count
    if vacuum_count != 1:
        errors.append("invalid_vacuum_count")

    nonintegral_depths: dict[str, int] = {}
    negative_depths: dict[str, int] = {}

    for character in candidate.characters:
        nonintegral_depth = first_nonintegral_depth(character)
        if nonintegral_depth is not None:
            nonintegral_depths[character.label] = nonintegral_depth

        negative_depth = first_negative_depth(character)
        if negative_depth is not None:
            negative_depths[character.label] = negative_depth

        if not character.coefficients:
            warnings.append(f"empty_coefficients:{character.label}")

    if nonintegral_depths:
        errors.append("nonintegral_coefficients")
        details["first_nonintegral_depths"] = nonintegral_depths

    if negative_depths:
        errors.append("negative_coefficients")
        details["first_negative_depths"] = negative_depths

    return ValidationResult(
        passed=not errors,
        errors=tuple(errors),
        warnings=tuple(warnings),
        details=details,
    )
