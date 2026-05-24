# AI-Amenable Open Problems in RCFT Modular-Bootstrap Classification

Date: 2026-05-24

## Executive conclusion

The strongest near-term target for this repository is **not** simply to generate more admissible RCFT character vectors. The literature has already pushed admissible and even partially tenable scans much further than a casual reading suggests. The sharper and more useful objective is to build an **exact, verifier-first classification stack** that separates:

1. generated candidate data,
2. admissible q-series data,
3. exact modular-data-reconstructible data,
4. Verlinde-passing / tenable data,
5. modular tensor category matched data,
6. known RCFT / VOA realized data,
7. genuinely unresolved candidates.

This distinction is essential because **admissible character vectors are not automatically realized RCFTs**. Recent holomorphic modular-bootstrap work explicitly distinguishes admissibility from stronger consistency conditions. The project should therefore avoid claiming that positive integer q-series imply physical realization.

The highest-value program is:

> Build a low-rank RCFT classification stack that ranks candidate MLDE/VVMF outputs by failure depth and exact tenability, then learns which candidates are most likely to survive full modular-data reconstruction and RCFT-consistency checks.

The most promising regime is **three to six characters**, modest Wronskian index, and bounded effective central charge. Two-character theories are the reproduction benchmark. Three-character theories are partially classified and useful for validation. Four to six characters are where exact computational tooling and AI-guided search can plausibly add value.

## Refined project thesis

The project should be organized around the rule:

> AI proposes search regions and pruning conjectures; exact arithmetic certifies every reported object.

The core research contribution should be an exact candidate ledger and staged validator, not a black-box neural model.

## Rank-by-rank landscape

| Rank regime | Current state | Best use in this project |
|---|---|---|
| `n = 1` | Meromorphic / holomorphic cases are heavily constrained. Useful for sanity checks. | Use as exact serialization, coefficient, and modular-phase tests. |
| `n = 2` | Mature. MMS, Hampapura-Mukhi, Chandra-Mukhi, Mason-Nagatomo-Sakai, and Mukhi-Rayhaun give strong baselines. | First serious reproduction target. Build golden tests. |
| `n = 3` | Partially classified in important Wronskian sectors. Quasi-character methods generate families. | First useful rejection-corpus and scan-comparison target. |
| `n = 4` | Low-rank bootstrap and small-genera results give strong constraints, but full classification remains open. | First target for exact S-reconstruction and tenability filtering. |
| `n = 5` | Allowed exponent constraints and bounded admissible scans exist, but realizability remains difficult. | AI-guided ranking and exact modular-data filtering become useful. |
| `n = 6` | Recent admissible/VVMF examples exist; complete classification is open. | High-upside target once verifier and reproduction benchmarks are stable. |

## What has already been tried

### MLDE / holomorphic modular bootstrap

The classic Mathur-Mukhi-Sen idea is to classify RCFTs by modular differential equations satisfied by their characters. Modern work treats character vectors as solutions of MLDEs and imposes modular covariance plus q-series integrality/positivity.

Strengths:

- clean symbolic formulation;
- exact rational exponents;
- strong relation to modular forms;
- well suited to low-character enumeration;
- can be implemented as deterministic recurrence generation.

Main failure modes:

- search space grows rapidly with rank, Wronskian index, and accessory parameters;
- admissible q-series may fail fusion;
- even fusion-consistent data may fail realization as an actual RCFT/VOA;
- direct MLDE scans become difficult beyond roughly three characters unless strong constraints are imposed.

### Vector-valued modular forms

The VVMF route treats the full character vector as a vector-valued modular form with multiplier representation. Recent work emphasizes this because direct MLDE searches become hard at higher rank.

Strengths:

- multiplier-preserving construction;
- natural route to ranks four through six;
- fits exact arithmetic and representation-theoretic filtering;
- good fit for AI search because candidate generation has structured algebraic provenance.

Main failure modes:

- VVMF generation can still produce admissible-looking but unrealized candidates;
- modular-data reconstruction remains nontrivial;
- known-theory matching and de-duplication become harder.

### Wronskian-index classification

Wronskian index `ell` organizes MLDE sectors and gives a compact way to compare known and generated character vectors.

Strengths:

- natural benchmark axis;
- used heavily in low-character classification literature;
- useful as a feature for AI ranking.

Main failure modes:

- Wronskian index alone is not enough to determine realization;
- high-index quasi-character families can create many admissible-looking objects;
- odd/even and pole-structure effects must be handled carefully.

### Hecke, coset, and quasi-character methods

Hecke operators, cosets, and quasi-characters provide constructive routes for generating new character data and organizing families.

Strengths:

- produce structured candidates rather than blind brute force;
- useful for known-theory matching and ancestry labels;
- likely useful as candidate-generator modules.

Main failure modes:

- can generate many descendants of already-known structures;
- novelty is easy to overstate unless duplicate and ancestry detection are strong.

### Fermionic and subgroup-aware RCFTs

Fermionic RCFTs naturally involve level-two congruence subgroups and spin structures, not only full `SL_2(Z)` bosonic modular behavior.

Strengths:

- strong integrality and congruence constraints;
- natural extension once bosonic baseline is stable;
- subgroup metadata gives useful model features.

Main failure modes:

- wrong subgroup assumptions produce wrong filters;
- candidate schema must explicitly store subgroup / spin-structure information.

## Key failure modes to design against

| Failure mode | Concrete risk | Repository response |
|---|---|---|
| Admissible = realized overclaim | Positive integer q-series are reported as RCFTs. | Store certificate stage explicitly. Never collapse stages. |
| Float contamination | Near-integers pass approximate tests and poison later checks. | Reject decimal input; use rational/algebraic exactness. |
| Late fusion failure | Expensive q-series candidates die only after Verlinde checks. | Add early modular-data and fusion hooks. |
| Duplicate rediscovery | Generated objects are known WZW/minimal/tensor/Hecke/coset relatives. | Build known-theory and ancestry matcher early. |
| Subgroup mismatch | Fermionic/spin cases are incorrectly treated as bosonic `SL_2(Z)` cases. | Add subgroup metadata to candidate schema. |
| Notebook-only research | Results cannot be replayed or audited. | Persist all candidates, failures, generator parameters, and hashes. |
| AI false positives | Model proposes plausible nonsense. | AI never certifies; exact validators certify. |

## Revised architecture

```text
published data + literature tables
        |
        v
known-theory database  <------ candidate generator registry
        |                         |      |       |
        |                         MLDE   VVMF    Hecke/coset/quasi-character
        v                         |
signature / ancestry matching     v
        |                   candidate ledger
        |                         |
        +-------------------------+
                                  |
                                  v
                            exact validator
                                  |
          +-----------------------+-----------------------+
          |                       |                       |
      rejected              admissible q-series       incomplete
   with witnesses                  |
          |                       v
          |              exact modular data layer
          |                       |
          |                       v
          |              Verlinde / fusion layer
          |                       |
          |                       v
          |                 tenable candidates
          |                       |
          |                       v
          |         known RCFT / MTC / VOA matching
          |                       |
          +-----------> AI ranking and pruning <----------+
```

## Immediate implementation implication

The current repository already has the right skeleton: exact rational parsing, candidate/character schemas, coefficient validators, first-failure depth, modular `T` helpers, a rational-S Verlinde sanity check, MLDE/VVMF scaffolds, tests, and CI.

The next code changes should add:

1. candidate certificate stages;
2. subgroup and generator provenance metadata;
3. a JSONL loader/validator CLI;
4. richer rejection labels and witness fields;
5. reference and known-theory data schemas;
6. benchmark suite names;
7. exact hash/provenance functions.

## Priority references

The core reference list is stored separately in:

- `docs/research/references.md`
- `data/references/rcft_core_references.jsonl`

## Research-backed project priorities

### Priority 1: exact staged certification

Do this before more generation. Every candidate should have a status ladder:

```text
generated -> schema_valid -> admissible -> modular_data_recovered -> verlinde_passing -> tenable -> matched_known -> unresolved_candidate
```

### Priority 2: known-theory benchmark database

Seed with:

- MMS two-character examples;
- Hampapura-Mukhi two-character cases;
- Chandra-Mukhi two-character data;
- Mukhi-Rayhaun unitary two-primary `c < 25` data;
- three-character Wronskian sectors;
- small-genera low-rank data;
- selected WZW/minimal/tensor product examples;
- fermionic level-two examples later.

### Priority 3: exact modular-data reconstruction

`T` is easy because `T_ii = exp(2*pi*i*(h_i - c/24))`. The hard part is exact `S`, cyclotomic representation, and Verlinde fusion. The repository should treat exact modular-data reconstruction as a core package, not as optional post-processing.

### Priority 4: rejection corpus

Rejected candidates are valuable. Store them with:

- generator parameters;
- failure stage;
- first failure depth;
- witness coefficient or witness fusion entry;
- content hash;
- exact rational fields.

This corpus becomes the first AI training set.

### Priority 5: AI only after exact labels exist

The first AI target should be a failure-depth ranker, not an RCFT generator. It should predict which candidates deserve expensive exact checks.

## Publication framing

The first plausible paper is not “AI discovers RCFTs.” A stronger and more defensible framing is:

> An exact-arithmetic certification and rejection-corpus pipeline for low-character RCFT modular-bootstrap candidates.

The second paper can be:

> AI-guided failure-depth prediction and pruning for MLDE/VVMF RCFT candidate searches.

The best result would be a bounded classification or strong exclusion table in a specific low-rank sector, with a public reproducible candidate ledger.
