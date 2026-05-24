from fractions import Fraction

from rcft.affine import AffineTheoryData
from rcft.io import read_jsonl


def test_affine_wzw_formula_for_a1_level_1():
    theory = AffineTheoryData.from_dict(
        {
            "algebra": "A1",
            "level": 1,
            "dimension_lie_algebra": 3,
            "dual_coxeter_number": 2,
            "nonvacuum_representation": "fundamental_2",
            "nonvacuum_representation_dimension": 2,
            "nonvacuum_quadratic_casimir": "3/4",
        }
    )

    assert theory.central_charge == Fraction(1, 1)
    assert theory.nonvacuum_conformal_weight == Fraction(1, 4)


def test_mms_wzw_target_manifest_has_expected_exact_values():
    records = list(read_jsonl("data/benchmarks/two_character/mms_wzw_targets.jsonl"))
    theories = {record["key"]: AffineTheoryData.from_dict(record) for record in records}

    assert theories["a1_1"].central_charge == Fraction(1, 1)
    assert theories["a1_1"].nonvacuum_conformal_weight == Fraction(1, 4)

    assert theories["g2_1"].central_charge == Fraction(14, 5)
    assert theories["g2_1"].nonvacuum_conformal_weight == Fraction(2, 5)

    assert theories["f4_1"].central_charge == Fraction(26, 5)
    assert theories["f4_1"].nonvacuum_conformal_weight == Fraction(3, 5)

    assert theories["e7_1"].central_charge == Fraction(7, 1)
    assert theories["e7_1"].nonvacuum_conformal_weight == Fraction(3, 4)


def test_affine_metadata_export_includes_derived_fields():
    record = next(read_jsonl("data/benchmarks/two_character/mms_wzw_targets.jsonl"))
    theory = AffineTheoryData.from_dict(record)
    metadata = theory.to_candidate_metadata()

    assert metadata["central_charge"] == "1"
    assert metadata["nonvacuum_conformal_weight"] == "1/4"
    assert metadata["wzw_denominator"] == 3
