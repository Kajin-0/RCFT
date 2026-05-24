# Implementation Path After Deep Research

## Strategic pivot

The project should be a **certification and rejection engine** before it is a candidate generator.

The literature makes one technical point unavoidable:

> A positive-integer character vector is not the same thing as a realized RCFT.

Therefore the repository must preserve certificate stages, exact witnesses, and provenance from the beginning.

## Work packages

### WP1: candidate ledger and CLI

Deliverables:

- JSONL reader/writer;
- deterministic content hash;
- `rcft-validate` command;
- `validated/` and `rejected/` output modes;
- machine-readable failure labels.

Acceptance test:

```bash
rcft-validate data/known_theories/toy_candidates.jsonl --out reports/validation/toy.jsonl
```

### WP2: exact q-series and MLDE baseline

Deliverables:

- recurrence utilities for low-order MLDEs;
- two-character reproduction dataset;
- scan configuration records;
- q-depth dependent failure statistics.

Acceptance test:

```text
known two-character benchmark records pass schema, q-series, and T-phase validation.
```

### WP3: known-theory database

Deliverables:

- reference-keyed source index;
- known-theory JSONL records;
- signature matcher;
- ancestry labels for WZW, minimal, tensor, coset, Hecke, quasi-character.

Acceptance test:

```text
candidate matching distinguishes exact duplicates from unresolved candidates.
```

### WP4: modular data layer

Deliverables:

- cyclotomic exact arithmetic plan;
- exact S/T record format;
- Verlinde fusion witness format;
- rank-small sanity checks.

Acceptance test:

```text
trivial and low-rank rational examples compute exact nonnegative fusion coefficients.
```

### WP5: VVMF higher-rank path

Deliverables:

- VVMF scan config;
- multiplier representation metadata;
- rank-four to rank-six literature reproduction targets;
- linear-combination candidate search.

Acceptance test:

```text
VVMF-generated records can be routed through the same validator and ledger.
```

### WP6: AI-guided pruning

Deliverables:

- rejected-candidate corpus;
- first-failure-depth features;
- simple baseline predictor;
- comparison against random scan ordering.

Acceptance test:

```text
AI-guided ordering reduces expensive q-depth expansions without losing known surviving candidates.
```

## File-level priorities

Immediate next files:

```text
rcft/io.py
rcft/hash.py
rcft/cli.py
tests/test_io.py
tests/test_hash.py
tests/test_cli.py
```

Then:

```text
data/benchmarks/two_character/*.jsonl
data/known_theories/*.jsonl
reports/validation/*.jsonl
```

## Non-goals for the next milestone

Do not yet implement:

- large neural networks;
- speculative quantum-gravity connections;
- full VOA realization proofs;
- high-rank brute-force scans;
- floating-point S-matrix checks.

## Milestone 1 definition

Milestone 1 is complete when the repository can:

1. load a JSONL candidate file;
2. validate each candidate exactly;
3. assign certificate stages;
4. emit rejected and accepted ledgers;
5. preserve failure witnesses;
6. run the whole path under CI.
