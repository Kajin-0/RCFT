from fractions import Fraction

import pytest

from rcft.qseries import add_series, coefficient_vector, multiply_series, truncate


def test_coefficient_vector_parses_exact_values():
    assert coefficient_vector(["1", "2/3", -1]) == (Fraction(1), Fraction(2, 3), Fraction(-1))


def test_truncate():
    assert truncate([Fraction(1), Fraction(2), Fraction(3)], 2) == (Fraction(1), Fraction(2))


def test_truncate_rejects_negative_precision():
    with pytest.raises(ValueError):
        truncate([], -1)


def test_add_series_with_padding():
    assert add_series([Fraction(1), Fraction(2)], [Fraction(3)], 3) == (
        Fraction(4),
        Fraction(2),
        Fraction(0),
    )


def test_multiply_series():
    assert multiply_series([Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)], 3) == (
        Fraction(1),
        Fraction(2),
        Fraction(1),
    )
