# Vendored AlphaGeometry 2 public symbolic core

Upstream repository: https://github.com/google-deepmind/alphageometry2

Original author: Google LLC. Copyright notices and Apache License 2.0 are retained verbatim.

Files: `ddar.py`, `elimination.py`, `numericals.py`, `parse.py`, `test.py`, `LICENSE`.

This is the **upstream public symbolic DDAR engine**, not independently rewritten GeoForge source. Vendoring gives access to the officially published symbolic component and its example tests. It does not provide the neural model, SKEST orchestration, synthetic 300M-scale training pipeline, or a universal Euclidean geometry solver.

The bundled files were retrieved from the upstream default branch on 2026-10-16. Source Git blob hashes:
- `ddar.py` — `012cfcd583f7f843ecfd9ddae73359a3e23db7c3`
- `elimination.py` — `49611d79251bd33fda953eb50e9e82b17833c901`
- `numericals.py` — `0eacf3b638882461acc16dc3c99cc7e8aaf1e4e0`
- `parse.py` — `dabf3ab8a808c9856134e480dffc36899ccee88d`
- `test.py` — `b5bd72621de04d8fa1a1ffeb5a5d4c4bc46cfad5`
- `LICENSE` — `d645695673349e3947e8e5ae42332d0ac3164cd7`

To test the reference implementation:

```bash
python vendor/alphageometry2_symbolic/test.py
python -m geoforge_prover.ddar2_reference examples
```
