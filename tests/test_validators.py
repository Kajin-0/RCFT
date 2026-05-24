from rcft.candidate_schema import Candidate
from rcft.validators import validate_candidate


def make_candidate(data):
    return Candidate.from_dict(data)


def test_validate_good_one_character_candidate():
    candidate = make_candidate(
        {
            "candidate_id": "toy_c0",
            "source": "unit_test",
            "n_characters": 1,
            "central_charge": "0",
            "q_precision": 4,
            "characters": [
                {"label": "vacuum", "h": "0", "coefficients": ["1", "1", "2", "3"]}
            ],
        }
    )
    result = validate_candidate(candidate)
    assert result.passed
    assert result.details["vacuum_count"] == 1


def test_validate_detects_nonintegral_coefficients():
    candidate = make_candidate(
        {
            "candidate_id": "bad_fraction",
            "source": "unit_test",
            "n_characters": 1,
            "central_charge": "0",
            "characters": [
                {"label": "vacuum", "h": "0", "coefficients": ["1", "1/2"]}
            ],
        }
    )
    result = validate_candidate(candidate)
    assert not result.passed
    assert "nonintegral_coefficients" in result.errors
    assert result.details["first_nonintegral_depths"] == {"vacuum": 1}


def test_validate_detects_negative_coefficients():
    candidate = make_candidate(
        {
            "candidate_id": "bad_negative",
            "source": "unit_test",
            "n_characters": 1,
            "central_charge": "0",
            "characters": [
                {"label": "vacuum", "h": "0", "coefficients": ["1", "-1"]}
            ],
        }
    )
    result = validate_candidate(candidate)
    assert not result.passed
    assert "negative_coefficients" in result.errors
    assert result.details["first_negative_depths"] == {"vacuum": 1}


def test_validate_detects_invalid_vacuum_count():
    candidate = make_candidate(
        {
            "candidate_id": "no_vacuum",
            "source": "unit_test",
            "n_characters": 1,
            "central_charge": "1",
            "characters": [
                {"label": "sector", "h": "1/2", "coefficients": ["1", "2"]}
            ],
        }
    )
    result = validate_candidate(candidate)
    assert not result.passed
    assert "invalid_vacuum_count" in result.errors
