# Family C: multiplicative structure

## Outcome

The literal rank-one ansatz, its reciprocal variant, rank-one
factorization of both \(u\) and \(v\), and rank one after centering all
collapse: either the row products \(N_i\) are equal or the positive
column differences \(d_j\) are equal.

There is a genuine non-collapsing rank-two construction with
arbitrarily many rows and two columns. It is a split-norm/divisor
construction and recovers the multiplicative mechanism behind the
known “arbitrarily many integers sharing two differences” result.

The standard Kronecker, split-complex, Gaussian-norm, and direct-block
compositions do not turn two smaller nondegenerate solutions into a
larger solution. The factor-pair tensor preserves row products but
loses column differences; the norm tensor can preserve a column
parameter but loses row products. Concrete counterexamples are in
`lemmas/tensor_composition_obstruction.md`.

No Pell-unit, Gaussian-integer, quaternion, or block construction found
here yields arbitrarily large square grids. In particular, nothing in
this note proves Erdős 885 for arbitrary \(k\).

## 1. The natural multiplicative algebra

Set

\[
s_{ij}=u_{ij}+v_{ij},\qquad d_j=v_{ij}-u_{ij}.
\]

Then

\[
s_{ij}^2-d_j^2=4N_i,\qquad
s_{ij}-d_j=2u_{ij},\qquad s_{ij}+d_j=2v_{ij}.               \tag{1}
\]

Thus the exact norm behind the problem is the split norm in

\[
\mathbb Q[\eta]/(\eta^2-1)\simeq\mathbb Q\times\mathbb Q,
\qquad
\operatorname{Nm}(s+d\eta)=s^2-d^2.
\]

This observation is useful but also exposes the obstruction.
Multiplying two split-norm elements multiplies their row norms, while
the new \(\eta\)-coordinate is \(se+dt\), which mixes source row data
\(s,t\) with source column data \(d,e\).

## 2. Rank-one ansätze

### 2.1 Literal rank one

For

\[
u_{ij}=x_i y_j,\qquad v_{ij}=\frac{N_i}{x_i y_j},
\]

the difference equation becomes

\[
\frac{N_i}{x_i}-x_i y_j^2=d_jy_j.                          \tag{2}
\]

Comparing two rows in (2) at two distinct positive \(y_j\)'s forces
both \(x_i\) and \(N_i/x_i\) to be equal across those rows, hence their
\(N_i\)'s are equal. If there are not two distinct \(y_j\)'s, the
columns coincide.

The same argument handles

\[
u_{ij}=x_i y_j,\qquad v_{ij}=z_iw_j.
\]

Row-product constancy first forces \(y_jw_j\) to be constant, reducing
the ansatz to a reciprocal pair. The centered rank-one proposal
\(s_{ij}=a_ib_j\) also collapses after comparing

\[
(a_i^2-a_h^2)b_j^2=4(N_i-N_h).
\]

Full proofs are in
`lemmas/rank_one_multiplicative_collapse.md`.

### 2.2 A surviving rank-two, two-column variant

Let

\[
M=t(t+1),\qquad \beta=2t+1,
\]

and index rows by proper divisors \(a<t\) of \(t\). Put \(b=M/a\).
The two centered columns

\[
s_{a1}=2(b-a),\qquad s_{a2}=2(b+a)
\]

have rank at most two as combinations of the row vectors \(a\) and
\(M/a\). The identity

\[
(b+a)^2-(b-a)^2=4M=\beta^2-1
\]

gives

\[
(b-a)^2-1=(b+a)^2-\beta^2.
\]

Consequently the two differences \(2\) and \(2\beta=4t+2\) occur for
every row product

\[
N_a=(b-a)^2-1.
\]

There are \(\tau(t)-1\) distinct such rows. Taking \(t\) to be a
product of \(m\) distinct primes gives \(2^m-1\) rows. See
`lemmas/two_column_divisor_construction.md` for the factor pairs,
positivity, distinctness, and the explicit \(3\times2\) example at
\(t=6\).

This is the closest multiplicative variant found that does not
collapse. Its limitation is exact: it supplies only two columns.

## 3. Composition of small solutions

Let one grid use \((u,v;N,d)\) and another use
\((p,q;M,e)\).

| Composition | Constraint preserved | Constraint lost |
|---|---|---|
| \(U=up,\ V=vq\) | \(UV=NM\), constant on composite rows | \(V-U=eu+dp+de\), dependent on both source rows |
| crossed \(U=uq,\ V=vp\) | \(UV=NM\) | \(V-U=dp-eu\), dependent on both source rows |
| \(S=st,\ D=de\) | \(D\) is constant on composite columns | \((S^2-D^2)/4=d^2M+e^2N+4NM\), dependent on columns |
| direct block sum | the two old diagonal blocks | off-diagonal blocks require all cross incidences in advance |

These formulas apply to \(2\times2\), \(3\times3\), and larger source
grids. Therefore increasing the source size does not repair the
standard tensor operation.

For a concrete \(2\times2\) counterexample, start with

\[
\begin{array}{c|cc}
N&d=2&d=26\\ \hline
1680&(40,42)&(30,56)\\
360 &(18,20)&(10,36).
\end{array}
\]

The \(d=2\) column of its parallel Kronecker square has differences
\(164,120,120,76\). All composite cells still have the correct
row-product \(N_iN_r\), but the composite column is not constant.

The dual failure is visible in the valid square-row table

\[
\begin{array}{c|cc}
N&d=15&d=48\\ \hline
100&(5,20)&(2,50)\\
324&(12,27)&(6,54).
\end{array}
\]

Taking \(S=st,D=de\) in the composite row \((100,100)\) gives products
\(85000\) and \(292900\) in two different columns. Here the proposed
composite differences are column-only, but row products are not
row-only.

This does not prove that every imaginable nonlinear composition is
impossible. It excludes the standard monomial Kronecker pairings, the
two split-norm/Brahmagupta pairings, the direct sum without separately
solving its cross blocks, and the direct Euclidean-norm tensor.

## 4. Gaussian and Hurwitz composition

The Gaussian norm is positive definite:

\[
\operatorname{Nm}_{\mathbb Z[i]}(a+bi)=a^2+b^2,
\]

whereas (1) uses \(s^2-d^2\). If \(N_i=m_i^2\) is itself a square, one
can encode a cell as

\[
z_{ij}=d_j+2m_i i,\qquad \operatorname{Nm}(z_{ij})=s_{ij}^2.
\]

Gaussian multiplication gives

\[
(d_j+2m_i i)(e_\ell+2n_r i)
=(d_je_\ell-4m_in_r)+2(d_jn_r+e_\ell m_i)i.                \tag{3}
\]

The candidate real coordinate in (3) depends on the composite row,
and the candidate half-imaginary coordinate depends on the composite
column. Thus norm multiplicativity produces valid Pythagorean
identities cell by cell but not the row/column separation required by
the grid. The \(N=100,324\) table above supplies a numerical
counterexample entirely inside \(\mathbb Z[i]\).

Moreover,

\[
\mathbb Z[i]^\times=\{\pm1,\pm i\},
\]

so Gaussian units alone provide only sign changes and quarter-turns,
not an unbounded family of distinct columns.

Quaternion and Hurwitz composition has the same structural mismatch.
It composes a positive-definite four-square norm. The table requires
one distinguished coordinate \(d_j\) and a complementary quantity
equal to the single row value \(4N_i\). Bilinear quaternion
multiplication mixes the distinguished coordinate with all
complementary coordinates. Restricting to two coordinates gives
exactly (3); instead retaining only the product \(S=st\) and the
column-only coordinate \(D=de\) gives the failing norm tensor in
Section 3. Extra quaternion coordinates do not by themselves supply
the missing separation.

This is an obstruction to the standard Hurwitz construction, not a
classification of all identities built from quaternions.

## 5. Pell units and quadratic-ring units

For a real quadratic unit, write

\[
x_n+y_n\sqrt{\Delta}=\alpha\varepsilon^n,\qquad
x_n^2-\Delta y_n^2=C.
\]

The direct assignment \(s=x_n,d=y_n\) gives

\[
s^2-d^2=C+(\Delta-1)y_n^2,
\]

so the required row product varies along every nontrivial orbit when
\(\Delta\ne1\). The assignment
\(d=\sqrt{\Delta}\,y_n\) restores the norm but loses rational, hence
integer, factor differences for nonsquare \(\Delta\).

A broader natural ansatz uses the two embeddings \(t,t^{-1}\):

\[
s_i(t)=A_it+B_i/t,\qquad d(t)=Ct+D/t.
\]

At three values with distinct \(t^2\), the conditions
\(s_i(t)^2-d(t)^2=4N_i\) force

\[
A_i=\pm C,\qquad B_i=\pm D,\qquad N_i\in\{0,-CD\}.
\]

Thus all positive rows collapse to one product. The polynomial proof
is in `lemmas/pell_laurent_collapse.md`. Two parameter values escape
the three-root argument, consistent with the genuine two-column
construction above.

Imaginary quadratic integer rings have finite unit groups, so their
units cannot index arbitrarily many columns. At \(\Delta=1\), the real
quadratic norm becomes the correct split norm, but the algebra is
\(\mathbb Q\times\mathbb Q\), not a Pell field. Its integral norm
equation is just

\[
(s-d)(s+d)=4N,
\]

and multiplicity comes from divisors rather than an infinite unit
orbit. That divisor mechanism is precisely what powers the
\(r\times2\) construction.

## 6. Final status

Concrete results:

1. Literal and centered rank-one multiplicative ansätze collapse.
2. The first non-collapsing split-norm variant gives \(r\times2\)
   grids for every \(r\).
3. Standard products of two small grids preserve at most one of the
   two defining constraints; explicit \(2\times2\) counterexamples
   witness both failure directions.
4. Natural Pell trace/anti-trace ansätze collapse at three columns,
   Gaussian units are finite, and Gaussian/Hurwitz norm multiplication
   mixes row and column data.

No construction here gives \(k\) distinct rows and \(k\) distinct
positive columns for arbitrary \(k\).
