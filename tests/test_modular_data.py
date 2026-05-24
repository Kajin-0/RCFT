from fractions import Fraction

from rcft.candidate_schema import Candidate
from rcft.modular_data import reduce_mod_one, t_phase_exponents_mod_one


def test_reduce_mod_one():
    assert reduce_mod_one(Fraction(-1, 6)) == Fraction(5, 6)
    assert reduce_mod_one(Fraction(7, 6)) == Fraction(1, 6)


def test_t_phase_exponents_mod_one():
    candidate = Candidate.from_dict(
        {
            "candidate_id": "toy_ising_like",
            "source": "unit_test",
            "n_characters": 2,
            "central_charge": "1/2",
            "characters": [
                {"label": "vacuum", "h": "0", "coefficients": ["1"]},
                {"label": "energy", "h": "1/2", "coefficients": ["1"]},
            ],
        }
    )
    assert t_phase_exponents_mod_one(candidate.characters) == (Fraction(47, 48), Fraction(23, 48))
