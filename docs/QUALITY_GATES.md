# Verifiable quality gates for GeoForge

The purpose of this document is to prevent substituting implementation volume, tests generated from a few formulas, or copied upstream code for scientific evidence.

## Non-negotiable mathematical contract

- A `proved` result must remain correct for **all admissible realizations** of the declared hypotheses. A symbolic polynomial identity alone does not establish nonzero, distinctness, incidence-order, or other side conditions.
- `counterexample` requires a fully checked model in which every premise is true and the goal is false. An unsuccessful random search means `unknown`, never refuted.
- `conditional` must expose every unproved guard. Proof checkers must recompile the source hypotheses and goal, rather than trusting the certificate's own declarations.
- The parsing, canonicalization, exact evaluation, algebraic compilation, and rule application of each supported predicate must implement the **same semantics**.
- No PR can claim parity with AG2 from a run of a vendored upstream DDAR2 solver, an internal mini-benchmark, or generated regression identities.

## Regression gates

Run the modular adversarial suite:

```bash
python -m pip install -r requirements.txt
python -m pytest -q tests_modular/
```

Run the deterministic certified prover and sample regression suite:

```bash
python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode quick --out local-results/quick.json
```

Run the extended locally generated matrix **when appropriate**:

```bash
python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode stress --out local-results/stress.json
```

Both `quick` and `stress` are **regression** suites. They are not a measurement of IMO solve rate.

## Six independent criteria for an evidence-based 10/10

A numerical 10/10 is a **future acceptance threshold**, not an assigned project score.

| Dimension | Evidence required before claiming 10/10 |
|---|---|
| Research value | Explicit original contribution and independently reproducible ablation against a state-of-the-art baseline |
| Independent mathematical implementation | Broad, documented formal-language coverage; independently replayable certificates; adversarial semantic soundness tests; differential tests against public DDAR2 |
| Functional breadth | End-to-end input formalization, nontrivial auxiliary search, proof output, and successful external use cases with documented limitations |
| Scientific validation | Disjoint, immutable challenge sets, hashes, fixed budgets, explicit timeouts, resource accounting, independent result checking, and publicly reproducible published benchmark results |
| Mathematical reliability | No known false positive, clearly scoped semantics, audits of all inference/degeneracy paths, formal checker hardening, and continuous adversarial differential testing |
| Production readiness | Reproducible environments, security and dependency management, CI across supported platforms, license clearance, observability, performance targets, maintained release process, and documented support/SLOs |

Benchmark procedure:

1. Pin an immutable commit SHA, Python/dependency versions, hardware, and time/memory budgets.
2. Use the SAME formal problem list and independent success checker for both the candidate and baseline.
3. Record solved/unknown/error/timeout independently, including proof replay and construction count.
4. Separate GeoForge's own symbolic solver, vendored DDAR2-only inference, deterministic auxiliary search, and optional learned-model search in the results.
5. Keep the complete per-problem outcomes and input dataset hashes; report failure cases and provide reproducible commands.
6. Publish a score only when the corresponding evidence is available. Otherwise use **not measured**, not an optimistic estimate.

## Known boundaries as of 2026-10-16

- The modular rule portfolio is deliberately small and the AG2 parser accepts only a documented subset.
- Exact rational auxiliary **construction** does not make the reference DDAR2 interface exact: upstream parsing converts coordinates to binary floating point. The resulting DDAR2 deductions must not be represented as stand-alone exact proof certificates.
- Full SKEST, pretrained AG2-comparable weights, universal real-algebraic decision, and official IMO-AG-30/50 and IMOSL-AG-30 evaluations are not established.
- CI and generated identity tests give evidence about engineering regression, **not** independent theorem-solving accuracy.
- Licenses for third-party vendored files and the repository's own source require separate consideration.

This gate is intentionally conservative: improvements to implementation or tests do not retroactively imply 10/10 scientific or production maturity.
