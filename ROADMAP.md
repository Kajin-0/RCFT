# RCFT AI Bootstrap Roadmap

## Project objective

Build a verifier-first research codebase for AI-assisted rational conformal field theory candidate discovery.

The central rule is:

> AI proposes; exact arithmetic disposes.

## Phase 1: exact candidate verifier

- Define immutable candidate and character schemas.
- Parse all rational values exactly.
- Reject decimal inputs at the data boundary.
- Validate vacuum-sector uniqueness.
- Validate nonnegative integer q-series coefficients.
- Record first failure depths for future AI-guided pruning.

## Phase 2: known-theory benchmarks

- Add minimal-model seed data.
- Add small WZW seed data.
- Add two-character literature examples.
- Add duplicate/signature matching.

## Phase 3: MLDE scans

- Implement low-order MLDE recurrence generation.
- Reproduce known two-character admissible character vectors.
- Extend to three-character scans.
- Persist rejected candidates with machine-readable failure labels.

## Phase 4: VVMF scans

- Add vector-valued modular-form construction tooling.
- Reproduce rank-four to rank-six examples from recent literature.
- Search nearby admissible linear combinations.

## Phase 5: AI-guided search

- Train candidate-ranking models on accepted and rejected scans.
- Learn failure-depth predictors.
- Cluster surviving unknown candidates.
- Use symbolic regression to conjecture coefficient identities.

## Phase 6: publication outputs

- Candidate database.
- Rejection taxonomy.
- Reproducible scan scripts.
- Paper-ready tables.
