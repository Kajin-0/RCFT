from fractions import Fraction

from rcft.generate import affine_target_to_skeleton_candidate
from rcft.io import read_jsonl
from rcft.validators import validate_candidate


def test_affine_target_to_skeleton_candidate():
    record = next(read_jsonl("data/benchmarks/two_character/mms_wzw_targets.jsonl"))
    candidate = affine_target_to_skeleton_candidate(record)

    assert candidate.candidate_id == "wzw_a1_1"
    assert candidate.n_characters == 2
    assert candidate.central_charge == Fraction(1, 1)
    assert candidate.characters[0].label == "vacuum"
    assert candidate.characters[0].h == Fraction(0, 1)
    assert candidate.characters[0].coefficients == (Fraction(1, 1),)
    assert candidate.characters[1].label == "fundamental_2"
    assert candidate.characters[1].h == Fraction(1, 4)
    assert candidate.characters[1].coefficients == (Fraction(2, 1),)
    assert candidate.metadata["skeleton_only"] is True
    assert candidate.metadata["q_series_status"] == "leading_terms_only"


def test_affine_skeleton_candidates_pass_basic_qseries_validation():
    records = list(read_jsonl("data/benchmarks/two_character/mms_wzw_targets.jsonl"))
    candidates = [affine_target_to_skeleton_candidate(record) for record in records]

    assert all(validate_candidate(candidate).passed for candidate in candidates)
