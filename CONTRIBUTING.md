# Contributing to GeoForge

Contributions should prioritize mathematical correctness and reproducibility over raw line counts.

1. Add a **minimal failing theorem** to the test suite before changing a rule. Include non-degeneracy side conditions.
2. Do not count numerical validation of one diagram as a universal proof.
3. Keep certificate generation and certificate verification independent: a verifier must not simply call the same prover again.
4. For constructive algorithms, test existence, uniqueness, multiple branches and degeneracy.
5. Run `python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode quick` before proposing changes; the stress suite is required for changes to mathematical kernels.
6. Document runtime, memory, platform, input language, and any explicit `unknown` behavior.
7. Never describe 30/30, AG2 parity, or universal solving as achieved unless an independent benchmark report and checked proofs support the claim.
8. Keep generated stress tests reproducible from their generator scripts.

No blanket license grant has yet been selected by the repository owner. Please resolve licensing before accepting external code contributions.
