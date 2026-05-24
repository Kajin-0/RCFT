"""Verlinde formula utilities.

The initial implementation is intentionally conservative and exact-friendly. Full
cyclotomic-number support should be added before using this for publication-grade
modular data.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = tuple[tuple[Fraction, ...], ...]


def validate_square_matrix(matrix: Matrix) -> None:
    n = len(matrix)
    if n == 0:
        raise ValueError("matrix must be nonempty")
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")


def verlinde_coefficients_rational_s(s_matrix: Matrix, vacuum_index: int = 0) -> dict[tuple[int, int, int], Fraction]:
    """Compute Verlinde coefficients for a rational S matrix.

    This covers simple exact test cases. General RCFTs usually require cyclotomic
    arithmetic rather than bare Fractions.
    """

    validate_square_matrix(s_matrix)
    n = len(s_matrix)
    if not 0 <= vacuum_index < n:
        raise ValueError("vacuum_index out of range")

    coeffs: dict[tuple[int, int, int], Fraction] = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total = Fraction(0)
                for m in range(n):
                    denominator = s_matrix[vacuum_index][m]
                    if denominator == 0:
                        raise ZeroDivisionError(f"S_0,{m} is zero")
                    total += s_matrix[i][m] * s_matrix[j][m] * s_matrix[k][m] / denominator
                coeffs[(i, j, k)] = total
    return coeffs


def all_fusion_coefficients_nonnegative_integers(coefficients: dict[tuple[int, int, int], Fraction]) -> bool:
    return all(value.denominator == 1 and value >= 0 for value in coefficients.values())
