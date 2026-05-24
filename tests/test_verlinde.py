from fractions import Fraction

from rcft.verlinde import all_fusion_coefficients_nonnegative_integers, verlinde_coefficients_rational_s


def test_verlinde_for_trivial_one_sector_theory():
    coeffs = verlinde_coefficients_rational_s(((Fraction(1),),))
    assert coeffs[(0, 0, 0)] == 1
    assert all_fusion_coefficients_nonnegative_integers(coeffs)


def test_verlinde_detects_noninteger_fusion():
    coeffs = {(0, 0, 0): Fraction(1, 2)}
    assert not all_fusion_coefficients_nonnegative_integers(coeffs)
