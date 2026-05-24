"""Command-line interface for RCFT candidate validation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from rcft.candidate_schema import CertificateStage
from rcft.hash import candidate_hash
from rcft.io import CandidateIOError, read_candidates, write_jsonl
from rcft.validators import validate_candidate


def validation_record(candidate) -> dict[str, object]:
    """Validate one candidate and return a machine-readable ledger record."""

    result = validate_candidate(candidate)
    stage = CertificateStage.ADMISSIBLE_Q_SERIES if result.passed else CertificateStage.REJECTED
    return {
        "candidate_id": candidate.candidate_id,
        "candidate_hash": candidate_hash(candidate),
        "input_certificate_stage": candidate.certificate_stage.value,
        "assigned_certificate_stage": stage.value,
        "passed": result.passed,
        "errors": list(result.errors),
        "warnings": list(result.warnings),
        "details": result.details,
        "candidate": candidate.to_dict(),
    }


def validate_file(input_path: Path, output_path: Path | None = None) -> tuple[int, int, list[dict[str, object]]]:
    """Validate an input JSONL file and optionally write an output JSONL report."""

    records = [validation_record(candidate) for candidate in read_candidates(input_path)]
    passed = sum(1 for record in records if record["passed"])
    failed = len(records) - passed
    if output_path is not None:
        write_jsonl(records, output_path)
    return passed, failed, records


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rcft-validate",
        description="Validate RCFT candidate JSONL ledgers using exact arithmetic.",
    )
    parser.add_argument("input", type=Path, help="Input JSONL candidate ledger.")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional output JSONL validation report path.",
    )
    parser.add_argument(
        "--fail-on-rejected",
        action="store_true",
        help="Exit with status 1 if any candidate is rejected.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        passed, failed, _records = validate_file(args.input, args.out)
    except (CandidateIOError, KeyError, ValueError, TypeError) as exc:
        print(f"rcft-validate: error: {exc}", file=sys.stderr)
        return 2

    total = passed + failed
    print(f"validated={total} passed={passed} rejected={failed}")
    if args.out is not None:
        print(f"wrote={args.out}")

    if args.fail_on_rejected and failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
