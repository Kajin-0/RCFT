from rcft.candidate_schema import Candidate, CertificateStage


def test_candidate_defaults_to_generated_stage_and_sl2z_subgroup():
    candidate = Candidate.from_dict(
        {
            "candidate_id": "toy",
            "source": "unit_test",
            "n_characters": 1,
            "central_charge": "0",
            "characters": [
                {"label": "vacuum", "h": "0", "coefficients": ["1"]}
            ],
        }
    )

    assert candidate.certificate_stage == CertificateStage.GENERATED
    assert candidate.subgroup == "SL2Z"
    assert candidate.provenance.method == "unknown"


def test_candidate_round_trips_certificate_and_provenance_metadata():
    candidate = Candidate.from_dict(
        {
            "candidate_id": "mlde_candidate",
            "source": "literature",
            "n_characters": 2,
            "central_charge": "4/5",
            "certificate_stage": "admissible_q_series",
            "subgroup": "SL2Z",
            "provenance": {
                "method": "mlde",
                "reference_key": "hampapura_mukhi_2015_two_characters",
                "parameters": {"ell": 0, "q_precision": 20},
            },
            "characters": [
                {"label": "vacuum", "h": "0", "coefficients": ["1", "1"]},
                {"label": "sector_1", "h": "1/5", "coefficients": ["1", "2"]},
            ],
        }
    )

    as_dict = candidate.to_dict()

    assert candidate.certificate_stage == CertificateStage.ADMISSIBLE_Q_SERIES
    assert as_dict["certificate_stage"] == "admissible_q_series"
    assert as_dict["provenance"]["method"] == "mlde"
    assert as_dict["provenance"]["reference_key"] == "hampapura_mukhi_2015_two_characters"
    assert as_dict["provenance"]["parameters"] == {"ell": 0, "q_precision": 20}
