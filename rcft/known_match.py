"""Known-theory matching utilities.

The first matcher is deliberately simple: compare central charge, conformal weights,
and an optional prefix of q-series coefficients. Later versions should account for
permutations, tensor products, extensions, Galois conjugates, and naming aliases.
"""

from __future__ import annotations

from rcft.candidate_schema import Candidate


def signature(candidate: Candidate, coefficient_depth: int = 10) -> tuple[object, ...]:
    weights = tuple(sorted(str(character.h) for character in candidate.characters))
    coeffs = tuple(
        tuple(str(value) for value in character.coefficients[:coefficient_depth])
        for character in sorted(candidate.characters, key=lambda item: (item.h, item.label))
    )
    return (str(candidate.central_charge), weights, coeffs)


def find_exact_signature_match(
    candidate: Candidate,
    known_candidates: list[Candidate],
    coefficient_depth: int = 10,
) -> Candidate | None:
    target = signature(candidate, coefficient_depth=coefficient_depth)
    for known in known_candidates:
        if signature(known, coefficient_depth=coefficient_depth) == target:
            return known
    return None
