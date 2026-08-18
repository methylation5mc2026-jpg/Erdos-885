# Family G: inductive lift \(k\to k+1\)

## Verdict

- No fourth or fifth positive integer \(N\) shares all four listed
  differences in either Guiduli seed or in the supplied Mausberg seed.
  This is an exhaustive divisor computation, not a bounded search.
- Each supplied triple has exactly the four displayed common positive
  differences, so there is no extra column either.
- A separate, explicitly verified Mausberg square-translate packet
  transposes to a positive \(4\times4\) pattern.  Its integer row fiber and
  its common-difference set both have cardinality exactly four.
- Imposing the fourth square on a one-dimensional candidate-row family
  produced no new rational point with reduced denominator at most \(20000\).
- No \(5\times5\) example was found.

A numerical \(k=5\) example, if found, would prove only the \(k=5\) case.
It would be progress toward Erdős 885, not a proof of the assertion for
all \(k\).

## Exhaustive row search for the supplied seeds

For two fixed differences \(d<e\), write

\[
x^2=4N+d^2,\qquad y^2=4N+e^2.
\]

Then

\[
(y-x)(y+x)=e^2-d^2.
\]

The positive divisor pairs of the fixed right-hand side therefore enumerate
every possible positive integer \(N\); see
`lemmas/fixed_two_differences_finite.md`.  Testing the remaining listed
differences gives:

| seed | candidates from first two differences | all survivors |
|---|---:|---|
| Guiduli 1 | 86 | \(6925500,37901500,108448956\) |
| Guiduli 2 | 86 | \(2778300,862552800,5400442044\) |
| Mausberg | 23 | \(79200,227205,1258560\) |

Thus the supplied lists are not merely the solutions below the earlier
square-root cutoff: they are the complete positive-integer fibers for those
four fixed differences.  In particular, there is no extra \(N\) to use as a
fourth or fifth row.

Direct factor-pair enumeration of each supplied \(N\) also gives the exact
intersections

\[
\begin{aligned}
\bigcap_{\text{Guiduli 1}}D(N)
  &=\{420,3780,14940,76860\},\\
\bigcap_{\text{Guiduli 2}}D(N)
  &=\{420,3780,61695,154332\},\\
\bigcap_{\text{Mausberg}}D(N)
  &=\{36,468,692,1028\}.
\end{aligned}
\]

So none of the fixed triples supplies an extra common difference.

## An independently checked \(4\times4\) pattern

Use the five integers

\[
330,\ 870,\ 2445,\ 4155,\ 10482
\]

and the three positive shifts

\[
756000,\ 15971200,\ 45130176.
\]

`compute/family_G_lift.py` directly checks that every \(y^2+a\) for these
five \(y\)'s and three \(a\)'s is a square.  Take \(y_0=330\).  The four
square roots at \(y_0\), including the zero shift, are

\[
x_j\in\{330,930,4010,6726\}.
\]

For the other four \(y_i\), set

\[
N_i=y_i^2-y_0^2,\qquad d_j=2x_j.
\]

The identity

\[
4N_i+d_j^2
=4(y_i^2-y_0^2)+4(y_0^2+a_j)
=4(y_i^2+a_j)
\]

proves the transpose construction without using Bremner's unavailable
parametrization.  Numerically,

\[
\begin{aligned}
(N_i)&=(648000,\ 5869125,\ 17155125,\ 109763424),\\
(d_j)&=(660,\ 1860,\ 8020,\ 13452).
\end{aligned}
\]

The square-root matrix \((s_{ij})\) is

\[
\begin{pmatrix}
1740&2460&8180&13548\\
4890&5190&9370&14298\\
8310&8490&11530&15798\\
20964&21036&22436&24900
\end{pmatrix}.
\]

Hence all sixteen identities \(s_{ij}^2=4N_i+d_j^2\) hold.  Applying the
exact two-difference fiber enumeration to these four \(d_j\)'s gives 57
candidates and exactly the four displayed \(N_i\).  Factoring the four
\(N_i\)'s gives exactly the four displayed common differences.  This fixed
pattern therefore has neither a fifth integer row nor a fifth integer
column.

## A one-dimensional \(4\to5\) row-lift attempt

Keep the four differences above and seek another row.  Put

\[
z^2=4N+660^2.
\]

Sharing the first three differences is the one-dimensional curve

\[
\begin{aligned}
u^2&=z^2+(1860^2-660^2)=z^2+3024000,\\
v^2&=z^2+(8020^2-660^2)=z^2+63884800.
\end{aligned}
\]

Its smooth projective normalization is a genus-one curve: it is the
biquadratic cover of the \(z\)-line branched at the four distinct roots of
\((z^2+3024000)(z^2+63884800)\).  The fourth difference imposes the one
additional square condition

\[
w^2=z^2+(13452^2-660^2)=z^2+180520704.
\]

Thus this is a literal one-extra-square lift attempt on a family constructed
from the verified \(4\times4\) pattern, not a quotation from Bremner.

For integer \(z\), the divisor lemma proves that the only positive rows are
the four already present, with

\[
z\in\{1740,4890,8310,20964\}.
\]

For a bounded rational check, write \(z=p/q\) in lowest terms.  The first
equation implies

\[
(r-p)(r+p)=3024000q^2.
\]

Enumerating all factor pairs for every \(1\le q\le20000\), then imposing
the other two square tests, checks \(2678511\) reduced positive candidates.
The only survivors are

\[
(p,q)=(1740,1),(4890,1),(8310,1),(20964,1).
\]

This denominator-bounded result is not a proof that the resulting
higher-genus curve has no further rational point.  A new rational point at
larger denominator could still give, after homogeneous scaling, a fifth
integer row sharing four differences.  Even that would leave the separate
task of finding a fifth common difference.

## Reproduction

Run:

```text
python3 compute/family_G_lift.py --max-denominator 20000
```

The seed results and integer fibers are exhaustive.  Only the rational
row-lift search has the stated denominator bound.

## Exact remaining gap

The cases \(k\le4\) are known.  This round supplies no \(k=5\) example and
no obstruction.  The immediate gap is a positive \(5\times5\) integer grid,
or a proof that none exists.  The gap to all \(k\) is larger: one must give
a construction for every \(k\ge5\), or disprove the conjecture at at least
one specific \(k\).  Solving \(k=5\) alone would not settle that all-\(k\)
gap.
