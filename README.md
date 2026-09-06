# Sharp Target-Domain Certificates for Quantum-Kernel Advantage under Distribution Shift

**Reproducibility artifact: code, frozen specifications, prediction locks, results, and manuscript sources.**

[![CI](https://github.com/roberto-fernandez-barrios/target-domain-certificates/actions/workflows/ci.yml/badge.svg)](https://github.com/roberto-fernandez-barrios/target-domain-certificates/actions/workflows/ci.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19147649.svg)](https://doi.org/10.5281/zenodo.19147649)
[![Release](https://img.shields.io/github/v/release/roberto-fernandez-barrios/target-domain-certificates)](https://github.com/roberto-fernandez-barrios/target-domain-certificates/releases)
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](LICENSE)
[![Python 3.11 | 3.12](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](pyproject.toml)

This repository accompanies the research article *Sharp Target-Domain Certificates for Quantum-Kernel Advantage under Distribution Shift* by Roberto Fernández-Barrios, Iker Pastor-López, Asier González-Santocildes, and Pablo García Bringas (Faculty of Engineering, University of Deusto). It contains the complete code path, the frozen analysis specifications, the physically separated prediction locks and audit labels, the versioned result inputs, and the LaTeX sources of the main text and the Supplementary Information, so that every table, figure, and number in the article can be inspected and regenerated.

**Status.** Research article submitted to EPJ Quantum Technology on 6 September 2026; an arXiv preprint has been submitted. The immutable snapshot of this repository is archived on Zenodo as version 1.1.6 ([10.5281/zenodo.21776862](https://doi.org/10.5281/zenodo.21776862)); the concept DOI [10.5281/zenodo.19147649](https://doi.org/10.5281/zenodo.19147649) always resolves to the latest version.

## What the article establishes

A claim of quantum predictive advantage under distribution shift usually requires the target labels. The article derives, for a fixed quantum candidate and a prespecified classical-kernel reference family, the assumption-free sharp interval of the finite-batch advantage that remains compatible with the target labels not yet inspected. The result holds for any additive bounded loss on a finite label space, is proved sharp and minimal, and for zero-one accuracy reduces to closed forms on the disagreement matrix that stay pathwise exact after any realized audit subset, including adaptively chosen labels. Nested reference families and partial label audits then define an evidence frontier: how much classical search and how much target supervision suffice to falsify a material advantage.

The certificate is embedded in a controlled quantum-kernel benchmark on eight fixed security shifts from EMBER, UNSW-NB15, and ToN-IoT, with entangling-ZZ and separable-product fidelity maps at 4-12 simulated qubits against 115 classical kernels, and it is corroborated prospectively on TableShift tasks whose predictions were locked and hashed before any target label was opened. Protocol controls reverse an apparent advantage; zero-label upper endpoints against the full family span 0.002-0.088; auditing 0-33 of 500 labels reduces every endpoint to at most 0.010; and finite-shot noise can increase predictive distinctness without useful advantage. The article claims neither classical simulability, hardware advantage, nor a complexity-theoretic separation.

![The controlled kernel-swap protocol](docs/assets/fig_v4_protocol.png)

## Study design at a glance

- **Three source datasets, eight fixed scenario-groups, two modalities.** EMBER (static PE malware) and the UNSW-NB15 (DoS, reconnaissance) and ToN-IoT (scanning) network-flow benchmarks.
- **Three shift mechanisms.** Label-conditional sparsity-tail and train-centroid-tail stress tests, plus a held-out attack-campaign shift on network traffic (an unseen attack campaign together with a capture-partition change; not a timestamped temporal split).
- **Kernel swap only.** Within each setting the preprocessing, samples, splits, classifier, tuning rule, and selection rule are shared; only the kernel changes. Two classifiers consume the same precomputed Gram matrices: a support-vector classifier (SVC) and a Laplace-approximation Gaussian-process classifier (GPC).
- **Thirty-five kernel geometries.** Twenty-three classical kernel-shape/scale blocks (linear, RBF, polynomial, Laplacian, Matern) and twelve fidelity feature-map blocks (two entangling ZZ maps, two separable product maps, three angle scales), each crossed with five embedding dimensions: 115 classical and 60 quantum candidates. Symmetric length-scale freedom; per-configuration regularization tuned by cross-validation on the training Gram matrix alone.
- **Target-label-free selection at equal budget (P1').** Deployment candidates are chosen on a disjoint in-distribution validation split, families are compared at matched 60-candidate budgets, and the full 115-candidate pool is kept as the deliberately adversarial reference for predictive indispensability.
- **Fixed-case inference.** Seventy-two principal settings with five q-split clusters, each holding three model-seed realizations; scenario-groups are reported as fixed cases with pointwise 95% conditional cluster-t intervals over the five clusters, with no population p-value.
- **Circuit-aware strata and finite-shot sensitivity.** Logical depth and CX counts for every feature map; 30 independent binomial measurement replicates at four shot counts under an unprojected estimate, an independent-square PSD heuristic, and a coherent train-based Nystrom extension, conditional on eight fixed exact Gram matrices (2,880 evaluations).
- **Prospectively frozen external validation.** College Scorecard, diabetes readmission, and ACS income from TableShift, with 30 audited task-size-seed units and 37,800 split-level results.
- **Sharp target-domain certificates.** A bounded-loss interval hull with sharpness and minimality, closed-form zero-one specialization, pathwise-exact partial-label contraction, a 30/60/115 reference-breadth frontier, and a prospectively specified Gate-2 replication against the prespecified classical-kernel reference family (BRFSS Diabetes, ACS Food Stamps, NHANES Lead), with prediction locks hashed before the one-time label opening.

## Main results

![Descriptive family contrasts under target-label-free, budget-matched selection](docs/assets/fig_v4_honest.png)

1. **Oracle selection manufactures an advantage.** Under same-test oracle selection with fixed regularization, fidelity kernels appear to beat linear+RBF baselines on EMBER by up to +0.037 OOD balanced accuracy under SVC; the gap shrinks to +0.004 once heavier-tailed classical kernels are admitted.
2. **The controlled comparison does not preserve it.** With regularization tuned on training data, selection without OOD labels, and matched budgets, the source-dataset-equal quantum-minus-classical difference against the equal-budget extended family is -0.00565 for SVC (leave-one-source-dataset-out range [-0.00702, -0.00450]) and -0.00094 for GPC ([-0.00190, +0.00094]); against the customary linear+RBF reference it is -0.00407 and +0.00591, with heterogeneous group signs. Intervals are conditional on five q-split clusters and are neither equivalence tests nor simultaneous intervals.
3. **Entanglement is not the missing ingredient.** Two of the four quantum maps are separable product kernels that factorize over coordinates. At matched 30-candidate budgets the source-dataset-equal SVC effect is -0.00928 for the entangling-ZZ stratum and -0.00547 for the product stratum; restricting the family to ZZ interactions does not reveal a hidden positive effect.
4. **Rank-matched pairing.** In an observational nearest-effective-rank pairing with a prespecified 1.25 caliper (75.2% of pairs retained), median quantum-minus-classical differences are negative in all eight scenario-groups; the result persists under alternative calipers and one-to-one matching and identifies no causal family effect.
5. **Evaluation choices interact.** The evaluation-choice 2x2x2x2 factorial moves the q1000 SVC endpoint from +0.0131 at its fixed-C, same-test-oracle, customary-reference, native-budget corner to -0.0047 at the fully controlled corner; train-CV regularization and the extended reference have the largest paired changes, but a +0.0139 interaction precludes additive or causal attribution. Removing frozen port-, protocol-, and service-related fields moves the two-network-source effect from -0.0031 to -0.0245, concentrated in the ToN-IoT campaign shift.
6. **Finite shots create distinctness without advantage.** At 128 shots the perturbed model disagrees with its exact-statevector counterpart on a median 7.2-7.4% of target decisions, yet the median increase in the full-family zero-label endpoint is only +0.003 to +0.009 and realized balanced accuracy does not improve. Effective rank from sampled fidelities is inflated by a median factor of 1.93 at 128 shots and 1.13 at 8,192 shots. The full four-shot-level sensitivity projects 4.24 trillion circuit shots before routing and device overhead.
7. **Protocol sensitivity is prospectively corroborated.** The prespecified cross-protocol map (S1-S10) spans +0.0475 to -0.0056 for SVC and +0.0418 to -0.0029 for GPC. On three external TableShift tasks frozen before result inspection, the task-equal controlled SVC effect is -0.0119 (95% conditional seed-cluster interval [-0.0205, -0.0033]) and the protocol contraction is +0.0208 ([+0.0113, +0.0307]); the GPC controlled effect is +0.0077 with an interval spanning zero.
8. **Sharp certificates against 115 classical kernels.** Zero-label upper endpoints range from 0.002 to 0.054 for SVC and from 0.006 to 0.088 for GPC. Across the frozen 30/60/115 reference breadths the cross-cell median endpoint contracts from 0.042 to 0.034 to 0.034. A fixed adaptive bottleneck-coverage audit reduces every endpoint to at most 0.010 with 0-33 of 500 labels (median 13 over 16 case-classifier cells); dynamic random-active and non-adaptive initial-coverage controls have median 12.5 and an exact ex-post label oracle 6.5, so the gain comes from restricting queries to actionable disagreements rather than from the coverage heuristic. The result persists for the selected entangling-ZZ models.
9. **Prospective Gate-2 corroboration against the prespecified classical-kernel reference family.** In the two technically eligible tasks, zero-label endpoints range from 0 to 0.168 (median 0.010), 11 of 20 cells already satisfy the 0.010 threshold without labels, the four task-classifier medians are 0-3 labels, the overall seed-level median is 0, the worst seed needs 76, and all 20 realized accuracy effects are negative (-0.156 to -0.002). NHANES Lead failed the prespecified 12-feature gate before any model was executed and was not replaced. All prospective quantum winners are product maps, so this replication does not independently validate the entangling stratum.

**Bottom line.** Under equal candidate budgets and target-label-free selection, the fixed low-qubit cases give no consistent evidence of an out-of-distribution advantage for the fidelity-kernel family over well-tuned classical kernels, and the sharp certificate turns "a classical model looks similar" into a falsification statement with an explicit materiality threshold and an explicit label cost. The three-gate reading separates protocol validity, target predictive indispensability, and quantum relevance, and none of the results is a claim about entanglement, hardware, or computational speedup.

![Nearest-rank paired differences are negative in all groups](docs/assets/fig_v4_rankmatched.png)

![External validation separates oracle and deployable conclusions](docs/assets/fig_v5_external.png)

## Repository layout

```text
src/
  utils/ember/        EMBER export and master/q-split construction
  utils/netflow/      network-flow export and shift constructions (m2-centroid, attack campaign)
  experiments/        kernel-swap runners (classical, quantum, extended + GPC)
  analysis/           kernel-geometry descriptors (effective rank, centered KTA)
scripts/
  ember/  netflow/    grid drivers (settings x seeds x sizes)
  experiments/        prediction export and lock stages (retrospective and prospective)
  analysis/           family comparisons, fixed-case inference, certificates, validators
  reporting/          every table and figure of the article, generated from results/
  reproduce_v4.py ... reproduce_v11.py   staged reproduction and audit drivers
  smoke/              CLI smoke test used by CI
results/              frozen per-run summaries, prediction locks, separated audit labels,
                      hashes, and versioned derived outputs (v4 to v10)
manuscript/           main text and Supplementary Information (LaTeX + PDF), bibliography,
                      Springer Nature class and style files, publication figures,
                      generated table rows
docs/                 frozen analysis specifications, prospective freeze records,
                      findings, validation status, release notes, README assets
tests/                scientific invariants, theorem checks, and artifact-integrity tests
ARTIFACT_MAP.md       component-to-reproducer map (what is frozen, what is regenerable)
CITATION.cff          software citation metadata (version 1.1.6)
PLAN.md               the v0.4 working plan (in Spanish) implemented by docs/ANALYSIS_SPEC_V4.md
```

## Reproduction

### Environment

Experiments were run with Python 3.11/3.12, NumPy 2.3.5, pandas 2.2.3, scikit-learn 1.8.0, Matplotlib 3.11.0, and Qiskit 2.3.1 (exact statevector fidelities; no hardware execution). The repository ships several dependency views for different purposes; see [`docs/REPRODUCIBILITY_NOTES.md`](docs/REPRODUCIBILITY_NOTES.md).

| File | Purpose |
|---|---|
| `environment.yml` | recommended Conda environment |
| `requirements.txt` / `requirements.lock.txt` | pinned pip environment / explicit pip snapshot |
| `environment.lock.yml` | Windows-specific Conda snapshot of the archival runs |
| `requirements-compat.txt` | looser compatibility envelope for non-archival installs |
| `requirements-gpu.txt` | optional CUDA acceleration of the exact fidelity Gram blocks |

```bash
conda env create -f environment.yml && conda activate kernel-shift-framework
pip install .
```

### Quick verification (minutes)

```bash
python -m pytest -q                              # 120 scientific-invariant and integrity tests
python scripts/smoke/smoke_test_cli.py           # CLI smoke test (writes docs/smoke_test_report.json)
python scripts/reproduce_v11.py --stage all      # theorem implementation, preservation ledger,
                                                 # reference-breadth summary, manuscript gates
```

### Full staged regeneration

Each driver consumes the frozen inputs of its generation and rebuilds the derived outputs, tables, and figures, then runs its integrity gates.

```bash
python scripts/reproduce_v4.py  --stage all   # provenance audit, controlled comparison, tables, figures
                                              # from the 1,080 frozen per-run summaries
python scripts/reproduce_v5.py  --stage all   # cross-protocol sensitivity map and frozen external validation
python scripts/reproduce_v6.py  --stage all   # estimand, matching, budget, and finite-shot gates
python scripts/reproduce_v8.py  --stage all   # circuit-aware strata, evaluation-choice factorial,
                                              # shortcut ablation, resource tables, integrity gates
python scripts/reproduce_v9.py  --stage all   # sharp retrospective certificates and evidence frontiers
python scripts/reproduce_v10.py --stage all   # prospective Gate-2 audit against the prespecified
                                              # classical-kernel reference family (hash-verified)
python scripts/reproduce_v11.py --stage all   # bounded-loss theorem, preservation ledger, manuscript gates
```

The reporting and audit stages deliberately consume versioned summaries and prediction locks rather than re-running the kernel experiments, which are computationally expensive; the grid drivers under `scripts/ember/` and `scripts/netflow/` regenerate them from the source datasets when needed.

### Source data

Raw datasets are not redistributed and remain subject to their original licenses: [EMBER](https://github.com/elastic/ember) (Anderson and Roth, 2018), [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset) (Moustafa and Slay, 2015), [ToN-IoT](https://research.unsw.edu.au/projects/toniot-datasets) (Alsaedi et al., 2020), and [TableShift](https://github.com/mlfoundations/tableshift) (Gardner et al., 2023; pinned at commit `fca9429814703a07e3902d005d46563a207b7f0a`). The repository stores derived split definitions, deterministic row-position hashes, shift constructions, and experiment manifests instead of raw records.

## Frozen specifications and integrity

Every analysis generation is governed by a specification written before its results were inspected; validators and tests check the specifications and the locked artifacts.

| Contract | Scope |
|---|---|
| [`docs/ANALYSIS_SPEC_V4.md`](docs/ANALYSIS_SPEC_V4.md) | controlled protocol: train-only regularization, target-label-free selection, budget matching, fixed-case inference |
| [`docs/EXTERNAL_VALIDATION_SPEC.md`](docs/EXTERNAL_VALIDATION_SPEC.md) | prospectively frozen TableShift external validation and cross-protocol map |
| [`docs/REVIEWER_REVISION_SPEC_V6.md`](docs/REVIEWER_REVISION_SPEC_V6.md), [`V7`](docs/REVIEWER_REVISION_SPEC_V7.md), [`V8`](docs/REVIEWER_REVISION_SPEC_V8.md) | estimand and matching controls, finite-shot sensitivity, circuit-aware strata and factorial |
| [`docs/PARTIAL_IDENTIFICATION_SPEC_V9.md`](docs/PARTIAL_IDENTIFICATION_SPEC_V9.md) | sharp zero-label and partial-label certificates, acquisition controls, finite-shot certificate |
| [`docs/GATE2_PROSPECTIVE_REPLICATION_SPEC_V10.md`](docs/GATE2_PROSPECTIVE_REPLICATION_SPEC_V10.md) and [`FREEZE_V10.json`](docs/GATE2_PROSPECTIVE_REPLICATION_FREEZE_V10.json) | prospective replication against the prespecified classical-kernel reference family: tasks, seeds, policies, thresholds, and numerical criteria fixed and hashed before acquisition; prediction locks, opaque label hashes, and the one-time opening record live under `results/v10/gate2_prospective/` |
| [`docs/V11_CONSOLIDATION_SPEC.md`](docs/V11_CONSOLIDATION_SPEC.md) | bounded-loss theory, preservation ledger, reference-breadth frontier |

`scripts/analysis/validate_manuscript_v8.py` through `validate_manuscript_v11.py` verify the SHA-256 of the frozen specifications and prediction locks, the numerical headline values, the manuscript format, and the absence of withdrawn terminology; the CI workflow runs them on every push together with the test suite and the smoke test. Findings are summarized in [`docs/V9_PARTIAL_IDENTIFICATION_FINDINGS.md`](docs/V9_PARTIAL_IDENTIFICATION_FINDINGS.md), [`docs/V10_GATE2_PROSPECTIVE_FINDINGS.md`](docs/V10_GATE2_PROSPECTIVE_FINDINGS.md), and [`docs/VALIDATION_STATUS.md`](docs/VALIDATION_STATUS.md); the editorial adaptation of the frozen manuscript is recorded in [`docs/EPJQT_EDITORIAL_ADAPTATION.md`](docs/EPJQT_EDITORIAL_ADAPTATION.md).

## Artifact levels and versions

GitHub holds the executable code, the frozen contracts, the manuscript sources, the tests, and the versioned result inputs consumed by the reproduction drivers (the `results/` tree is large by design). Zenodo holds the immutable release snapshots with the compiled PDFs, source bundle, release notes, and checksums. See [`ARTIFACT_MAP.md`](ARTIFACT_MAP.md) for the component-level map and [`docs/RELEASE_NOTES_V116.md`](docs/RELEASE_NOTES_V116.md) for the release history.

| Version | DOI | Role |
|---|---|---|
| all versions | [10.5281/zenodo.19147649](https://doi.org/10.5281/zenodo.19147649) | concept DOI |
| v1.1.6 | [10.5281/zenodo.21776862](https://doi.org/10.5281/zenodo.21776862) | curated final artifact (cite this) |
| v1.1.5 | [10.5281/zenodo.21764577](https://doi.org/10.5281/zenodo.21764577) | bibliographic and submission closure |
| v1.1.4 | [10.5281/zenodo.21759058](https://doi.org/10.5281/zenodo.21759058) | final submission artifact |
| v1.1.3 | [10.5281/zenodo.21751137](https://doi.org/10.5281/zenodo.21751137) | sharp target-domain certificates |
| v0.8.0 | [10.5281/zenodo.21717074](https://doi.org/10.5281/zenodo.21717074) | circuit-aware controlled comparison |

## Citation

Please cite the archived software release ([`CITATION.cff`](CITATION.cff)) and, once published, the research article.

```bibtex
@software{fernandezbarrios2026certificates,
  author  = {Fern{\'a}ndez-Barrios, Roberto and Pastor-L{\'o}pez, Iker and
             Gonz{\'a}lez-Santocildes, Asier and Garc{\'i}a Bringas, Pablo},
  title   = {Sharp Target-Domain Certificates for Quantum-Kernel Advantage
             under Distribution Shift},
  version = {1.1.6},
  year    = {2026},
  doi     = {10.5281/zenodo.21776862},
  url     = {https://github.com/roberto-fernandez-barrios/target-domain-certificates}
}
```

## Authors

- Roberto Fernández-Barrios (corresponding author, [roberto.fernandez.b@deusto.es](mailto:roberto.fernandez.b@deusto.es)), ORCID [0009-0003-5312-2634](https://orcid.org/0009-0003-5312-2634)
- Iker Pastor-López, ORCID [0000-0002-3068-6248](https://orcid.org/0000-0002-3068-6248)
- Asier González-Santocildes, ORCID [0009-0002-8888-8560](https://orcid.org/0009-0002-8888-8560)
- Pablo García Bringas, ORCID [0000-0003-3594-9534](https://orcid.org/0000-0003-3594-9534)

Faculty of Engineering, University of Deusto, Bilbao, Spain.

## License

BSD-3-Clause (see [`LICENSE`](LICENSE)). Benchmark datasets remain subject to their original licenses.
