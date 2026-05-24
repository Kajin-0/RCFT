from fractions import Fraction

import pytest

from rcft.exact import is_integer, parse_fraction, parse_fraction_list


def test_parse_fraction_accepts_exact_strings():
    assert parse_fraction("1/3") == Fraction(1, 3)
    assert parse_fraction("-47/48") == Fraction(-47, 48)
    assert parse_fraction(2) == Fraction(2, 1)


def test_parse_fraction_rejects_decimals():
    with pytest.raises(ValueError):
        parse_fraction("0.5")


def test_parse_fraction_list():
    assert parse_fraction_list(["1", "2/3"]) == (Fraction(1), Fraction(2, 3))


def test_is_integer():
    assert is_integer(Fraction(3, 1))
    assert not is_integer(Fraction(3, 2))
