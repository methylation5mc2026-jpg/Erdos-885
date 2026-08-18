# Round 2 log

Round 1 established the workspace, equivalences, literature file, and the
seven method families. Round 2 ran independent constructions and an
adversarial pass. There is still no proof for every \(k\), and no \(k=5\)
example.

## Proved in this repository (natural language)

- Lemma A and the matrix / homogeneity / anchored forms (`docs/equivalences.md`, `lemmas/lemma_A_square_criterion.md`).
- Finiteness of integer \(n\) sharing two **fixed** differences (`lemmas/fixed_two_differences_finite.md`).
- Non-existence of a nondegenerate separated identity \(A(x)+D(y)^2=S(x,y)^2\) (`lemmas/no_separated_rational_identity.md`).
- Common-parameter identities for \(k=2\) and \(k=3\) (`lemmas/common_parameter_grid_identities.md`).
- Genus of a common-translate curve with \(m\) offsets: \(g=1+2^{m-2}(m-3)\) (`lemmas/common_translate_curve_genus.md`).
- Rank-one multiplicative collapse; two-column divisor construction; tensor obstruction (`lemmas/rank_one_multiplicative_collapse.md`, `two_column_divisor_construction.md`, `tensor_composition_obstruction.md`, `pell_laurent_collapse.md`).
- Uniform real and \(p\)-adic solubility for every \(k\) (`lemmas/uniform_local_solubility.md`).
- Reconstruction of the Jiménez-Urroz mechanism: the curve
  \(Y^2=X(X-49140)(X-37620)\) has a non-torsion point, hence arbitrarily
  many integers sharing three differences after scaling
  (`research/family_A_elliptic.md`).
- Exhaustive fibres of the Guiduli and Mausberg seeds, and of the
  verified \(4\times4\) pattern (`research/family_G_lift.md`).

## Verified examples

| \(k\) | \(N\) | common differences | notes |
|------:|-------|--------------------|-------|
| 2 | 192, 2640 | 16, 26 | `examples/k2.txt` |
| 3 | 112, 952, 3240 | 6, 54, 111 | `examples/k3.txt`; elliptic reconstruction |
| 4 | 26128575, 291722431, 561117375, 713526975 | 126, 16110, 33390, 75390 | `examples/k4.txt`; complete intersection of size 4 |
| 4 | 648000, 5869125, 17155125, 109763424 | 660, 1860, 8020, 13452 | Mausberg \(Y\)-set transpose |
| 3+ | Guiduli / Mausberg \(3\times4\) | four diffs, three \(N\) | not \(k=4\) |

## Negative computational results (not disproofs)

- Extra-column search on \(\{112,952,3240\}\) returns exactly \(\{6,54,111\}\).
- The same three points plus \(2P\), after \(\lambda=36047\), share exactly the three scaled differences. No fourth column.
- Mausberg’s five integer \(z\)-values have exactly three positive offsets. No sixth integer \(z<5\cdot10^4\). Small Mordell–Weil combinations on \(Y(a,b)\) fail \(z^2+c\) square.
- Choudhry \((4,4)\) and \((5,3)\) tables have no admissible square-side translate with reduced denominator \(\le20000\).
- No unrestricted or square-side \(5\times5\) additive table with cell roots \(\le2000\).

## Family status after the audit

See `research/method_families.md` and `research/audit.md`. Families A
(general \(k\)) remains blocked. Families B, C, D, F, G remain active
with explicit missing lemmas. Family E is active and low priority.

## Distance to a complete solution

The original problem is open. The precise missing object is recorded in
`lemmas/missing_for_all_k.md`. The next round should not write a survey;
it should attempt one of those four objects, independently inside the
registered families.
