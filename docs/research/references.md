# RCFT Core References

This file is a working reference index for the RCFT project. It prioritizes sources that directly affect implementation strategy: MLDEs, VVMFs, Wronskian index, low-rank classification, modular data, fermionic/subgroup-aware RCFTs, AI-assisted CFT work, and exact-computation tooling.

## Foundational RCFT / MLDE

| Reference | URL | Project role |
|---|---|---|
| Mathur, Mukhi, Sen, *On the Classification of Rational Conformal Field Theories* | https://www.sciencedirect.com/science/article/pii/0370269388917650 | Original MLDE/character-classification idea. |
| Mathur, Mukhi, Sen, *Reconstruction of Conformal Field Theories From Modular Geometry on the Torus* | https://inspirehep.net/literature/267364 | Foundational reconstruction viewpoint. |
| Naculich, *Differential equations for rational conformal characters* | https://inspirehep.net/literature/262133 | Early modular differential equation work. |
| Verlinde, *Fusion Rules and Modular Transformations in 2D Conformal Field Theory* | https://www.sciencedirect.com/science/article/pii/0550321388901249 | Fusion from modular data; basis for Verlinde layer. |
| Di Francesco, Mathieu, Senechal, *Conformal Field Theory* | https://link.springer.com/book/10.1007/978-1-4612-2256-9 | Standard background reference. |

## Two-character classification benchmarks

| Reference | URL | Project role |
|---|---|---|
| Hampapura, Mukhi, *On 2d Conformal Field Theories with Two Characters* | https://arxiv.org/abs/1510.04478 | First serious benchmark suite for reproduction. |
| Chandra, Mukhi, *Towards a Classification of Two-Character Rational Conformal Field Theories* | https://arxiv.org/abs/1810.09472 | Extended two-character classification and quasi-characters. |
| Mason, Nagatomo, Sakai, *Vertex Operator Algebras with Two Simple Modules* | https://arxiv.org/abs/1803.11281 | VOA realization benchmark for two-module cases. |
| Mukhi, Rayhaun, *Classification of Unitary RCFTs with Two Primaries and Central Charge Less Than 25* | https://arxiv.org/abs/2208.05486 | Hard ground truth for unitary two-primary RCFTs. |

## Three-character and Wronskian-index classification

| Reference | URL | Project role |
|---|---|---|
| Franc, Mason, *Classification of some vertex operator algebras of rank 3* | https://arxiv.org/abs/1905.07500 | Rank-three VOA benchmark. |
| Das, Gowdigere, Santara, *Classifying three-character RCFTs with Wronskian index equalling 0 or 2* | https://arxiv.org/abs/2002.01949 | `n=3`, `ell=0,2` benchmark. |
| Gowdigere, Kala, Santara, *Classifying three-character RCFTs with Wronskian index equalling 3 or 4* | https://arxiv.org/abs/2308.01149 | `n=3`, `ell=3,4` benchmark. |
| Das, Gowdigere, Kanade, Mukhi, Santara, *Wronskian Indices and Rational Conformal Field Theories* | https://arxiv.org/abs/2012.14939 | Wronskian-index organization and known-theory comparison. |

## Holomorphic modular bootstrap / higher rank

| Reference | URL | Project role |
|---|---|---|
| Kaidi, Lin, Parra-Martinez, *Holomorphic modular bootstrap revisited* | https://arxiv.org/abs/2107.13557 | Allowed exponent constraints and `d <= 5` structure. |
| Govindarajan, Santara, *Two approaches to the holomorphic modular bootstrap* | https://arxiv.org/abs/2503.23761 | VVMF route; important for `n=4..6`. |
| Govindarajan, Sadanandan, *Updating the holomorphic modular bootstrap* | https://arxiv.org/abs/2604.11277 | Exact-S and bounded admissible scans up to six characters. |
| Govindarajan, Sadanandan, *S-matrices in the holomorphic modular bootstrap approach* | https://arxiv.org/abs/2602.14665 | Exact S-matrix reconstruction focus. |

## VVMF, Hecke, cosets, movable poles

| Reference | URL | Project role |
|---|---|---|
| Bantay, Gannon, *Vector-valued modular functions for the modular group and the hypergeometric equation* | https://arxiv.org/abs/hep-th/0512011 | VVMF theoretical foundation. |
| Gannon, *The theory of vector-modular forms for the modular group* | https://arxiv.org/abs/1310.4458 | VVMF machinery. |
| Harvey, Wu, *Hecke Relations in Rational Conformal Field Theory* | https://arxiv.org/abs/1804.06860 | Hecke candidate generation. |
| Duan, Lee, Sun, *Hecke Relations, Cosets and the Classification of 2d RCFTs* | https://arxiv.org/abs/2206.07478 | Structural generation and ancestry matching. |
| Das, Mukhi, Santara, *Modular Differential Equations with Movable Poles and Admissible RCFT Characters* | https://arxiv.org/abs/2308.00069 | Later extension after baseline MLDE/VVMF. |

## Fermionic / subgroup-aware RCFT

| Reference | URL | Project role |
|---|---|---|
| Bae, Duan, Lee, Lee, Song, *Fermionic Rational Conformal Field Theories and Modular Linear Differential Equations* | https://arxiv.org/abs/2010.12392 | Level-two congruence subgroups and fermionic MLDEs. |
| Bae, Duan, Lee, Lee, Song, *Bootstrapping Fermionic Rational CFTs with Three Characters* | https://arxiv.org/abs/2108.01647 | Fermionic three-character benchmark. |
| Duan, Lee, Li, Sun, *On Classification of Fermionic Rational Conformal Field Theories* | https://arxiv.org/abs/2210.06805 | Integrality and subgroup constraints. |
| Lee, Sun, *Hecke Relations among 2d Fermionic RCFTs* | https://arxiv.org/abs/2211.15304 | Fermionic Hecke extension. |

## Modular data / MTC matching

| Reference | URL | Project role |
|---|---|---|
| Ng, Rowell, Wang, Wen, *Reconstruction of modular data from SL2(Z) representations* | https://arxiv.org/abs/2203.14829 | Reconstruction/matching layer. |
| Ng, Rowell, Wang, Wen, *Classification of modular data up to rank 11* | https://arxiv.org/abs/2308.09670 | Low-rank modular-data database target. |
| SL2Reps GAP package | https://snw-0.github.io/sl2-reps/ | Possible congruence-kernel representation tool. |

## AI and formalization

| Reference | URL | Project role |
|---|---|---|
| Kantor, Niarchos, Papageorgakis, *Solving Conformal Field Theories with Artificial Intelligence* | https://arxiv.org/abs/2108.08859 | Evidence AI can help CFT search. |
| Krippendorf, Syvaeri, *Conformal Bootstrap with Reinforcement Learning* | https://arxiv.org/abs/2108.09330 | Bootstrap search with RL. |
| Cao et al., *Reconstructing Conformal Field Theoretical Composition with Transformers* | https://arxiv.org/html/2605.01072v1 | Rational-token transformer precedent. |
| Douglas et al., *Formalization of QFT* | https://arxiv.org/abs/2603.15770 | Formal-verification precedent. |

## Toolchain

| Tool | URL | Project role |
|---|---|---|
| SageMath | https://www.sagemath.org/ | Modular forms, q-expansions, Hecke, affine Lie algebra support. |
| Sage modular forms docs | https://doc.sagemath.org/html/en/reference/modfrm/index.html | Implementation reference. |
| PARI/GP | https://pari.math.u-bordeaux.fr/ | Fast modular/arithmetic kernels. |
| GAP | https://www.gap-system.org/ | Group and representation tools. |
| SDPB | https://github.com/davidsd/sdpb | Optional arbitrary-precision numerical bootstrap tool. |
| SymPy | https://www.sympy.org/ | Lightweight exact symbolic Python layer. |
| Lean 4 | https://lean-lang.org/ | Future proof kernels. |
| mathlib4 | https://github.com/leanprover-community/mathlib4 | Formal mathematics library. |
| pytest | https://docs.pytest.org/ | Test framework. |
| Ruff | https://docs.astral.sh/ruff/ | Linter. |
| GitHub Actions | https://docs.github.com/actions | CI. |
