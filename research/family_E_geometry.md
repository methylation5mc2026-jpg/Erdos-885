# Family E: geometric re-embedding

## Verdict

The odd-distance motivation of Erdős–Rosenfeld is historically important
and is **not** a viable attack on the remaining cases of Erdős 885.

Piepmeyer already solved the planar odd-integral-distance Turán problem
by a different construction. Re-embedding the square-grid equations as a
rational-distance configuration, an Euler brick, or a lattice problem on
the hyperbolas \(xy=N_i\) produces statements of the same strength as
885, not weaker ones. No incomplete reduction in this family is treated
as progress.

## What the 1997 geometry actually asks

Erdős asked whether \(n\) points in the plane can realise \(n^2/3\) odd
integral distances. Four points cannot form an odd-distance \(K_4\), so
Turán's theorem forces the extremal graph to be a balanced complete
tripartite graph. Erdős–Rosenfeld tried:

- \(2n\) points \(\bigl(\pm(2k_i+1)/2,\,0\bigr)\) on the \(x\)-axis,
- \(n\) points \((0,p_k)\) on the \(y\)-axis,

with every axis-to-axis distance an odd integer. That forces each
\(4p_k^2\) to have the same \(n\)-element set \(\{4k_i+2\}\) inside its
factor-difference set. The arithmetic abstraction is 885; the geometry
is a special case with extra parity and axis-alignment constraints.

Piepmeyer, *Discrete Comput. Geom.* **16** (1996), 113–115, constructed
arbitrarily large finite odd-integral-distance sets matching the Turán
bound without solving the axis-aligned Diophantine problem. The
geometric necessity of 885 is therefore gone. The number-theoretic
question remains.

## Other geometric realisations (incomplete reductions)

The rectangle identity \(s_{ij}^2+s_{i'j'}^2=s_{ij'}^2+s_{i'j}^2\) is
the same numerical condition that appears in:

- rational-distance subsets of the plane (Pythagorean, not odd-distance);
- Euler bricks / perfect cuboids (three face diagonals, or the space
  diagonal, being integral);
- integer-sided triangles with a common altitude, or Heron triangles
  with a common square translate (this *does* give the \(k=3\) identity
  in family B, via the second common square translate \(h\));
- lattice points on the rectangular hyperbolas \(xy=N_i\) whose vertical
  separations are independent of \(i\).

Each of these is a dictionary, not a solution. Translating 885 into the
perfect-cuboid problem, or into an unsolved rational-distance problem,
is an incomplete reduction: the target is open and of comparable
difficulty. Family B already extracted the one geometric identity that
*does* help, the Heron/Euler \(3\times3\) square translate, and recorded
its obstruction to a fourth column in
`lemmas/common_translate_curve_genus.md`.

## What would count as progress in this family

A reduction of the \(k\times k\) grid, for every \(k\), to a solved
distance problem (for example a theorem that a certain rational-distance
configuration exists for all \(k\)), with the extra constraints of 885
preserved. No such reduction is known. Until one appears this family
stays low priority and independent of the elliptic-slice work in family
A.

## Round-2 status

- Active, low priority.
- No new mechanism.
- Do not reopen as a general-\(k\) attack without a solved target
  problem.
