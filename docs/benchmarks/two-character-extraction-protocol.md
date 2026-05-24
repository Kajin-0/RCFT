# Two-Character Benchmark Extraction Protocol

This protocol prevents the project from ingesting unreliable benchmark records.

## Rule

Do not add a two-character candidate record unless the source location and extraction status are explicit.

Each benchmark candidate should include:

```json
{
  "candidate_id": "source_specific_unique_id",
  "source": "literature",
  "n_characters": 2,
  "central_charge": "exact rational",
  "wronskian_index": 0,
  "certificate_stage": "generated",
  "subgroup": "SL2Z",
  "provenance": {
    "method": "mlde|quasi_character|coset|voa_classification|manual_extraction",
    "reference_key": "hampapura_mukhi_2015_two_characters",
    "parameters": {
      "table": "exact table label or section",
      "row": "exact row label",
      "q_precision": "number of coefficients extracted"
    }
  },
  "characters": [
    {"label": "vacuum", "h": "0", "coefficients": ["..."]},
    {"label": "sector_1", "h": "exact rational", "coefficients": ["..."]}
  ],
  "metadata": {
    "extraction_note": "what was copied and how",
    "realization_status": "unknown|admissible_only|realized|excluded|claimed_candidate",
    "symmetry_or_identification": "optional text"
  }
}
```

## Certificate interpretation

Use `certificate_stage = generated` for extracted records unless this repository has revalidated the record itself.

After running `rcft-validate`, records may be assigned:

```text
admissible_q_series
```

This means only that the current q-series validator passed. It does not imply modular data, Verlinde fusion, or VOA/RCFT realization.

## Source priority

### First-pass two-character sources

1. `hampapura_mukhi_2015_two_characters`
   - Use for MLDE/Wronskian-index reproduction.
   - Especially important for `ell = 0,2,3,4` character-level candidates.

2. `chandra_mukhi_2018_two_character_classification`
   - Use for quasi-character and infinite-family structure.
   - Important for candidate ancestry and Hecke/quasi-character detection.

3. `mukhi_rayhaun_2022_two_primaries`
   - Use for realized/unitary RCFT benchmark.
   - Do not mix this with merely admissible character benchmarks.

4. `mason_nagatomo_sakai_2018_two_modules`
   - Use for VOA realization cross-checks.

## Extraction stages

| Stage | Meaning |
|---|---|
| `pending_manual_extraction` | Source identified but no records copied. |
| `raw_extracted` | Records copied but not independently validated. |
| `schema_validated` | Records parse into `Candidate`. |
| `q_series_validated` | Coefficients passed integrality/positivity/vacuum checks. |
| `cross_checked` | Records cross-checked against a second source or known-theory match. |

## Rejection policy

If a record fails validation, do not delete it. Move or copy it into a rejected ledger with:

- exact source key;
- table/row information;
- validator error labels;
- first failure depth;
- candidate hash.

Failures are scientifically useful because they can indicate transcription errors, convention mismatches, or real admissibility boundaries.
