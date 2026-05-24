import json

import pytest

from rcft.io import CandidateIOError, read_candidates, read_jsonl, write_jsonl


def test_read_jsonl_ignores_blank_lines_and_comments(tmp_path):
    path = tmp_path / "records.jsonl"
    path.write_text('\n# comment\n{"a": 1}\n', encoding="utf-8")

    assert list(read_jsonl(path)) == [{"a": 1}]


def test_read_jsonl_rejects_non_object_record(tmp_path):
    path = tmp_path / "records.jsonl"
    path.write_text("[1, 2, 3]\n", encoding="utf-8")

    with pytest.raises(CandidateIOError):
        list(read_jsonl(path))


def test_write_jsonl_round_trip(tmp_path):
    path = tmp_path / "nested" / "records.jsonl"
    write_jsonl([{"b": 2, "a": 1}], path)

    assert path.exists()
    assert json.loads(path.read_text(encoding="utf-8")) == {"a": 1, "b": 2}


def test_read_candidates(tmp_path):
    path = tmp_path / "candidates.jsonl"
    path.write_text(
        '{"candidate_id":"toy","source":"unit_test","n_characters":1,'
        '"central_charge":"0","characters":[{"label":"vacuum","h":"0","coefficients":["1"]}]}\n',
        encoding="utf-8",
    )

    candidates = list(read_candidates(path))
    assert len(candidates) == 1
    assert candidates[0].candidate_id == "toy"
