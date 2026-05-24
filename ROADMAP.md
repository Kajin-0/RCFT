# RCFT AI Bootstrap Roadmap

## Project objective

Build a verifier-first research codebase for AI-assisted rational conformal field theory candidate discovery, certification, rejection analysis, and known-theory matching.

The central rule is:

> AI proposes; exact arithmetic disposes.

## Refined strategy after literature review

The project should not merely generate admissible q-series. The literature already shows that admissible character vectors can be misleading: positive integer coefficients do not automatically imply an actual RCFT or VOA realization.

The project will therefore classify every object by a staged certificate ladder:

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

The highest-value output is a reproducible ledger of candidates, rejections, exact witnesses, and known-theory matches.

## Phase 1: exact candidate verifier

- Define immutable candidate and character schemas.
- Parse all rational values exactly.
- Reject decimal inputs at the data boundary.
- Validate vacuum-sector uniqueness.
- Validate nonnegative integer q-series coefficients.
- Record first failure depths for future AI-guided pruning.
- Add explicit certificate-stage fields.
- Add subgroup and generator-provenance metadata.

## Phase 2: CLI and ledger infrastructure

- Add `rcft-validate` CLI for JSONL candidate files.
- Persist validated records with deterministic content hashes.
- Persist rejected records with witness fields.
- Use failure labels as future AI training targets.

## Phase 3: known-theory benchmarks

- Add minimal-model seed data.
- Add small WZW seed data.
- Add two-character literature examples.
- Add Wronskian-index metadata.
- Add duplicate/signature matching.
- Add ancestry labels for tensor products, cosets, Hecke images, and quasi-character families.

## Phase 4: two-character MLDE reproduction

- Implement low-order MLDE recurrence generation.
- Reproduce Mathur-Mukhi-Sen style two-character examples.
- Reproduce Hampapura-Mukhi and Chandra-Mukhi benchmark cases.
- Compare against Mason-Nagatomo-Sakai and Mukhi-Rayhaun realization results where applicable.

## Phase 5: three-character benchmark scans

- Reproduce `n=3`, `ell=0,2` examples.
- Reproduce `n=3`, `ell=3,4` examples.
- Store complete rejection corpus with first-failure depths.
- Build scan-comparison reports.

## Phase 6: modular data and Verlinde layer

- Extend exact `T` phase support.
- Add exact cyclotomic representation for `S` matrices.
- Implement exact Verlinde fusion coefficient checks.
- Store fusion witnesses for rejection.
- Compare low-rank modular data against known classification tables.

## Phase 7: VVMF route for higher rank

- Add vector-valued modular-form construction tooling.
- Reproduce rank-four to rank-six examples from recent literature.
- Search nearby admissible linear combinations.
- Prioritize exact-S and tenability checks over raw candidate volume.

## Phase 8: AI-guided search

- Train candidate-ranking models on accepted and rejected scans.
- Learn failure-depth predictors.
- Cluster surviving unknown candidates.
- Use symbolic regression to conjecture coefficient identities.
- Use LLMs only for code generation, literature extraction, and conjecture proposals.

## Phase 9: publication outputs

- Candidate database.
- Rejection taxonomy.
- Exact witness ledger.
- Reproducible scan scripts.
- Known-theory matching tables.
- Paper-ready tables and figures.

## First publishable target

A defensible first paper is:

> An exact-arithmetic certification and rejection-corpus pipeline for low-character RCFT modular-bootstrap candidates.

A follow-up target is:

> AI-guided failure-depth prediction and pruning for MLDE/VVMF RCFT candidate searches.
