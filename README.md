# RCFT

AI-assisted modular-bootstrap tooling for rational conformal field theory candidate discovery, certification, rejection analysis, and known-theory matching.

This repository is initialized as a verifier-first research codebase. The immediate goal is to build exact-arithmetic infrastructure for character-vector validation, then extend toward modular-linear-differential-equation (MLDE), vector-valued modular-form (VVMF), modular-data, and AI-guided failure-depth workflows.

## Current status

The scaffold currently contains:

- exact rational parsing with decimal rejection;
- immutable `Candidate` and `Character` data schemas;
- explicit certificate stages so admissible q-series are not confused with realized RCFTs;
- generator provenance and subgroup metadata;
- q-series coefficient-vector utilities;
- JSONL candidate-ledger I/O;
- deterministic SHA-256 candidate hashing;
- validator functions for vacuum uniqueness, integrality, positivity, and first-failure depth;
- exact modular `T`-phase exponent helpers;
- a rational-S Verlinde sanity-check implementation;
- MLDE and VVMF scan configuration scaffolds;
- `rcft-validate` CLI;
- unit tests and GitHub Actions CI.

## Install

```bash
git clone https://github.com/Kajin-0/RCFT.git
cd RCFT
python -m pip install -e '.[dev]'
```

Optional SageMath-oriented environment:

```bash
conda env create -f environment.yml
conda activate rcft-ai-bootstrap
python -m pip install -e '.[dev]'
```

## Run tests

```bash
pytest -q
ruff check .
```

## Validate a candidate ledger

```bash
rcft-validate data/known_theories/toy_candidates.jsonl --out reports/validation/toy.jsonl
```

Expected summary format:

```text
validated=1 passed=1 rejected=0
wrote=reports/validation/toy.jsonl
```

The output ledger contains the candidate hash, input stage, assigned stage, errors, warnings, exact failure witnesses, and the canonical candidate record.

## Minimal candidate record

```json
{
  "candidate_id": "toy_c0",
  "source": "manual",
  "n_characters": 1,
  "central_charge": "0",
  "q_precision": 4,
  "certificate_stage": "generated",
  "subgroup": "SL2Z",
  "provenance": {
    "method": "manual",
    "reference_key": null,
    "parameters": {}
  },
  "characters": [
    {"label": "vacuum", "h": "0", "coefficients": ["1", "1", "2", "3"]}
  ]
}
```

## Certificate ladder

```text
generated
  -> schema_valid
  -> admissible_q_series
  -> modular_data_recovered
  -> verlinde_passing
  -> tenable
  -> matched_known
  -> unresolved_candidate
```

Rejected candidates are stored with witness information instead of being discarded.

## Design rule

AI can propose candidate regions, code, conjectures, and pruning rules. Exact arithmetic validates every reported object.
