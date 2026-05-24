from rcft.candidate_schema import Candidate
from rcft.hash import candidate_hash, canonical_json, sha256_json


def test_canonical_json_sorts_keys():
    assert canonical_json({"b": 2, "a": 1}) == '{"a":1,"b":2}'


def test_sha256_json_is_order_independent():
    assert sha256_json({"a": 1, "b": 2}) == sha256_json({"b": 2, "a": 1})


def test_candidate_hash_is_deterministic():
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

    assert candidate_hash(candidate) == candidate_hash(candidate)
