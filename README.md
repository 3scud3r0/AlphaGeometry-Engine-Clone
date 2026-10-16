# GeoForge — AlphaGeometry Engine Clone (research prototype)

> **Unofficial, independently developed research project.** GeoForge is inspired by Google DeepMind's AlphaGeometry and AlphaGeometry 2. It is **not** a reproduction of the complete AlphaGeometry 2 system, is not endorsed by Google DeepMind, and has **not** demonstrated 30/30 on the official IMO-AG-30 or 100% on any official olympiad benchmark.

**Repository description:** Experimental neuro-symbolic and deterministic geometry theorem prover in Python, with exact algebra, auxiliary-construction search, replayable proof certificates, synthetic data generation, and a seven-phase regression suite.

## Features implemented in the current source

- A prototype deductive geometry engine (DD/AR-inspired), numerical diagram realization, symbolic facts, selected theorem rules, and synthetic problem generation.
- **Training-free deterministic proof attempt** (`upgrade prove-deterministic`): bounded symbolic inference, exact rational/affine and polynomial techniques, rational counterexample search, and conditional certificates where side conditions remain open.
- **Independent proof replay** (`upgrade check-deterministic`) for the supported certificate formats.
- Exact-geometry utilities for points, lines, circles, homogeneous coordinates, inversion, radical axes, and selected symbolic constructions.
- Optional Transformer/Mixture-of-Experts demonstration code (not trained AG2 model weights).
- Synthetic datasets, generated tests, a miniature local benchmark, and a 450-requirement audit. **Passing local tests is not evidence of olympiad-level parity.**

The package also contains experiments and research implementations with **limited domain coverage**. Check the [parity roadmap](docs/ROADMAP_AG2_E_UNIVERSALIDADE.md) for what is not yet implemented.

## Requirements and installation

Python **3.11+** recommended. Linux/macOS/Windows where the dependencies are available.

```bash
git clone https://github.com/3scud3r0/AlphaGeometry-Engine-Clone.git
cd AlphaGeometry-Engine-Clone
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

PyTorch is **optional** and needed only for neural demonstration commands:

```bash
python -m pip install -r requirements-neural.txt
```

## Prove a geometric statement without training a model

```bash
python geoforge.py upgrade prove-deterministic \
  --given 'midp d a b' \
  --given 'midp e a c' \
  --given 'ncoll a b c' \
  --goal 'para d e b c' \
  --timeout 5 \
  --out proof.json

python geoforge.py upgrade check-deterministic --path proof.json
```

The example encodes the triangle midsegment theorem: `d` is the midpoint of `ab`, `e` is the midpoint of `ac`, the triangle is non-collinear, and the goal is `de ∥ bc`.

Typical status labels:

| Status | Meaning |
|---|---|
| `proved` | Proved within a supported formalism, with a replayable certificate. |
| `counterexample` | An exact rational diagram satisfying the assumptions and falsifying the goal was found. |
| `conditional` | An algebraic identity was obtained, but a required side condition is **not** established. Not a proof of the original goal. |
| `unknown` | No proof or counterexample was found within the configured budget. Neither true nor false is established. |
| `invalid_problem` | A recognized invalid or contradictory input was detected; not a complete inconsistency decision procedure. |

To explore other commands:

```bash
python geoforge.py --help
python geoforge.py upgrade --help
```

## Exact geometric constructions

See [`examples/construcoes.json`](examples/construcoes.json):

```bash
python geoforge.py upgrade construct-exact \
  --input examples/construcoes.json \
  --out pontos_exatos.json
```

Constructing one diagram is **not** a proof of a universally quantified theorem.

## Tests and benchmarks

Run the quick deterministic regression:

```bash
python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode quick
```

Run the local stress suite (requires more time):

```bash
python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode stress
```

Or run the project-specific tests:

```bash
python -m pytest -q geoforge_upgrade_suite/tests/
python geoforge_7fases_benchmark.py --mode quick
```

The generated stress matrices live under `geoforge_upgrade_suite/tests/` and `geoforge_upgrade_suite/matrix_untrained/`. The original generator scripts are also included. The report files in the repository are **snapshots from previous local executions**, not newly verified GitHub Actions results. The 12-case mini-benchmark is **not** IMO-AG-30 or IMO-AG-50.

GitHub Actions runs a short CI gate; full stress runs can be launched manually.

## Project layout

```text
geoforge.py                                 Original entry point + upgrade commands
geoforge_upgrade_suite/
    deterministic_solver.py                 Bounded exact/certified proof attempt
    deterministic_ideal.py                  Polynomial ideal techniques
    saturation_solver.py                    Conditional algebraic saturation
    affine_certificate.py                   Exact affine witnesses
    exact_constructions.py                  Exact symbolic constructions
    geometry_exact.py                       Exact geometry and transformations
    symbolic_coordinates.py                 Algebraic coordinate representation
    reasoning_search.py                     Experimental multi-branch search
    formal_language.py                     Conservative problem formalization
    dataset_engineering.py                 Synthetic data handling
    neural_baseline.py                     Optional neural demonstration
    tests/                                  Unit and stress tests
    matrix_untrained/                       Deterministic generated regression cases
geoforge_7fases_benchmark.py                Seven-phase audit runner
auditoria_450/                              Requirement inventory and prior snapshots
EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py    One-command local test gate
docs/ROADMAP_AG2_E_UNIVERSALIDADE.md          Proposed modules and acceptance criteria
```

## Relationship to AlphaGeometry 2

AlphaGeometry 2 reported 30/30 on IMO-AG-30, 42/50 on IMO-AG-50, and 20/30 on IMOSL-AG-30 under its published experimental protocols. **No comparable official result has been established for GeoForge.** The public DDAR2 code does not include all proprietary models, weights, large-scale training resources, and search infrastructure needed to reproduce the full system.

A claim of **universal geometry solving** needs a precisely defined input language and model of computation. A complete decision procedure exists in theory for first-order sentences over real closed fields, but its worst-case complexity is severe, and this does not entail a solver for every conceivable mathematical/geometric problem.

Read the [technical roadmap](docs/ROADMAP_AG2_E_UNIVERSALIDADE.md) for a detailed list of source files to implement and independent pass/fail milestones.

## References and attribution

- [Google DeepMind AlphaGeometry](https://github.com/google-deepmind/alphageometry)
- [Google DeepMind AlphaGeometry 2 — public DDAR2 code](https://github.com/google-deepmind/alphageometry2)
- [AlphaGeometry 2 paper (JMLR)](https://www.jmlr.org/papers/volume26/25-1654/25-1654.pdf)

**Licensing:** No open-source license has been selected for this independently developed repository as part of this publication. Contributors should not assume rights beyond those granted by applicable law. Any third-party sources and future dependencies must retain their own notices and licenses; no official AlphaGeometry source code is claimed to have been copied into GeoForge.

## Contributing and reproducibility

See [`CONTRIBUTING.md`](CONTRIBUTING.md). A feature should only be marked *validated* when it has executable tests and, for mathematical inferences, a proof certificate or a valid refutation. Please report unsupported theorem families as `unknown`, rather than presenting them as disproved.
