# Lean 4

Formalisation is **blocked**.

The project rule is: a natural-language proof of Erdős 885 for every
\(k\) (or a complete disproof for some \(k\)) must survive the
adversarial log `research/audit.md` before any Lean theorem is written.
That proof does not exist in this repository.

Do not add a `sorry` theorem, an unaudited axiom, or a formalisation of
an equivalent unproved restatement. mathlib arithmetic would be
acceptable as a dependency once there is a proof to formalise; it is
not a substitute for one.

When a surviving proof appears, this directory should become a Lake
package stating only audited lemmas, starting from Lemma A
(`d ∈ D(n) ↔ 4n + d^2` is a square) and ending at the full conjecture.
