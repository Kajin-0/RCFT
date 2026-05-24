import json

from rcft.cli import main, validate_file


def test_validate_file_writes_report(tmp_path):
    input_path = tmp_path / "candidates.jsonl"
    output_path = tmp_path / "report.jsonl"
    input_path.write_text(
        '{"candidate_id":"toy","source":"unit_test","n_characters":1,'
        '"central_charge":"0","characters":[{"label":"vacuum","h":"0","coefficients":["1","2"]}]}\n',
        encoding="utf-8",
    )

    passed, failed, records = validate_file(input_path, output_path)

    assert passed == 1
    assert failed == 0
    assert len(records) == 1
    assert output_path.exists()
    report = json.loads(output_path.read_text(encoding="utf-8"))
    assert report["candidate_id"] == "toy"
    assert report["assigned_certificate_stage"] == "admissible_q_series"
    assert report["passed"] is True
    assert "candidate_hash" in report


def test_main_returns_success_for_valid_file(tmp_path, capsys):
    input_path = tmp_path / "candidates.jsonl"
    input_path.write_text(
        '{"candidate_id":"toy","source":"unit_test","n_characters":1,'
        '"central_charge":"0","characters":[{"label":"vacuum","h":"0","coefficients":["1"]}]}\n',
        encoding="utf-8",
    )

    status = main([str(input_path)])

    captured = capsys.readouterr()
    assert status == 0
    assert "validated=1 passed=1 rejected=0" in captured.out


def test_main_can_fail_on_rejected(tmp_path):
    input_path = tmp_path / "candidates.jsonl"
    input_path.write_text(
        '{"candidate_id":"bad","source":"unit_test","n_characters":1,'
        '"central_charge":"0","characters":[{"label":"vacuum","h":"0","coefficients":["1/2"]}]}\n',
        encoding="utf-8",
    )

    status = main([str(input_path), "--fail-on-rejected"])

    assert status == 1
