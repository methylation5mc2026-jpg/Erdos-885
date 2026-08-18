# Family F: local solubility and possible disproof

## Verdict

There is **no real or \(p\)-adic obstruction** for \(k=5\) or \(k=6\).
In fact, `lemmas/uniform_local_solubility.md` gives a nondegenerate local
point for every \(k\) at every place.

This is not evidence of a local--global theorem and is not a proof of
Erdős 885.  The integral, positive, simultaneous square problem remains.

## The real place

For either \(k=5\) or \(6\), and indeed for arbitrary \(k\), set

\[
N_i=i,\qquad d_j=j,\qquad s_{ij}=\sqrt{4i+j^2}.
\]

This is a real solution with the required positivity and distinctness.

## The prime 2: squares modulo 8 and 16

Set \(N_i=2i\) and \(d_j=2j-1\).  Then

\[
4N_i+d_j^2=8i+(2j-1)^2\equiv1\pmod8.
\]

Hence every entry is a square in \(\mathbb Z_2\).  At the requested finite
levels:

- squares modulo \(8\) are \(0,1,4\), and every entry above is \(1\);
- squares modulo \(16\) are \(0,1,4,9\).  An odd square is \(1\) or \(9\),
  and adding \(8i\) merely interchanges \(1\) and \(9\).

The integers \(2,4,\ldots,2k\) are genuinely distinct in \(\mathbb Z_2\),
as are \(1,3,\ldots,2k-1\), even though some have equal residues modulo a
small power of 2.

## Every odd prime, including 5 and 7

For an odd prime \(p\), set

\[
N_i=pi,\qquad d_j=1+pj.
\]

Then

\[
4N_i+d_j^2=1+p(4i+2j+pj^2).
\]

Thus every entry is \(1\pmod p\).  For \(p=5\), the square residues are
\(0,1,4\); for \(p=7\), they are \(0,1,2,4\).  In both cases the displayed
entry is the residue \(1\).  More importantly, Hensel's lemma at the simple
root \(X=1\) lifts the root through every power \(p^r\), so this is a
\(\mathbb Z_p\)-solution, not merely a modulo-\(p\) check.

The same proof handles every odd prime.  The script
`compute/local_solubility.py` checks the residue formulas for \(k=5,6\),
modulo \(8,16\), and for a sample of odd primes including \(5,7\).

## Why the apparent small-modulus obstruction is false

Global distinctness does not imply distinctness modulo a chosen modulus.
For example, \(p,2p,\ldots,kp\) are distinct in \(\mathbb Z_p\) but all
reduce to zero modulo \(p\).  Requiring \(k\) distinct residues for the
\(N_i\) or \(d_j\) therefore tests a stronger, irrelevant problem and can
manufacture false negatives when \(k\) exceeds the number of suitable
residue classes.

The affine congruence equations also have completely collapsed solutions,
so a useful local check should meet the open conditions \(N_i\ne N_{i'}\)
and \(d_j\ne d_{j'}\).  The constructions above do meet those conditions
as exact \(p\)-adic inequalities.

## Disproof status

No local obstruction was found.  The explicit local points prove that no
obstruction at any single real or \(p\)-adic place exists for this system,
for \(k=5,6\) or any larger \(k\).  A disproof, if one exists, must use a
genuinely global/integral obstruction rather than failure of local
solubility.
