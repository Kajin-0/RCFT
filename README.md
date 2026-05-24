# RCFT

AI-assisted modular-bootstrap tooling for rational conformal field theory candidate discovery.

This repository is initialized as a verifier-first research codebase. The immediate goal is to build exact-arithmetic infrastructure for character-vector validation, then extend toward modular-linear-differential-equation (MLDE) and vector-valued modular-form (VVMF) scans.

## Current status

The initial scaffold contains:

- exact rational parsing with decimal rejection;
- immutable `Candidate` and `Character` data schemas;
- q-series coefficient-vector utilities;
- validator functions for vacuum uniqueness, integrality, positivity, and first-failure depth;
- exact modular `T`-phase exponent helpers;
- a rational-S Verlinde sanity-check implementation;
- MLDE and VVMF scan configuration scaffolds;
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

## Minimal candidate record

```json
{
  "candidate_id": "toy_c0",
  "source": "manual",
  "n_characters": 1,
  "central_charge": "0",
  "q_precision": 4,
  "characters": [
    {"label": "vacuum", "h": "0", "coefficients": ["1", "1", "2", "3"]}
  ]
}
```

## Design rule

AI can propose candidate regions, code, conjectures, and pruning rules. Exact arithmetic validates every reported object.
