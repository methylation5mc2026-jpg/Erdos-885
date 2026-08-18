# Erdős Problem 885

Research workspace for the Erdős–Rosenfeld conjecture on common factor differences.

## Problem

For \(n\ge 1\),

\[
D(n)=\bigl\{\lvert a-b\rvert:n=ab\bigr\}.
\]

**Conjecture.** For every integer \(k\ge 1\) there exist \(N_1<\cdots<N_k\) such that

\[
\bigl\lvert\textstyle\bigcap_{i=1}^k D(N_i)\bigr\rvert\ge k.
\]

Status: proved for \(k=2\) (Erdős–Rosenfeld 1997), \(k=3\) (Jiménez-Urroz 1999), \(k=4\) (Bremner 2019). Open for general \(k\). This repository does **not** contain a proof for every \(k\), nor a disproof. Round 2 of the research system, including the adversarial audit and the concrete missing lemma, is in `research/round2.md`, `research/audit.md`, and `lemmas/missing_for_all_k.md`.

## Layout

- `docs/` — literature review and equivalent formulations
- `research/` — method-family registry and round logs
- `lemmas/` — statements that have been proved or refuted
- `compute/` — reproducible searches and checks
- `examples/` — explicit numerical configurations
- `paper/` — manuscript (only a complete proof belongs here as a claimed theorem)
- `lean/` — Lean 4 formalization (started after a surviving natural-language proof)

## Success criterion

A complete proof for every \(k\ge 1\) (or a complete disproof for some \(k\)), surviving adversarial audit, then Lean 4 verification. Reductions to unproved conjectures, fixed-\(k\) numerics, and unproved candidate counterexamples do not count as a solution.
