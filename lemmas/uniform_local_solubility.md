# Uniform local solubility of the grid

## Lemma

For every \(k\geq 1\), the system

\[
s_{ij}^{\,2}=4N_i+d_j^2 \qquad (1\leq i,j\leq k)
\]

has a real point with positive, pairwise distinct \(N_i\) and positive,
pairwise distinct \(d_j\).  For every prime \(p\), it also has a
\(\mathbb Z_p\)-point for which the \(N_i\) are pairwise distinct and the
\(d_j\) are pairwise distinct (as \(p\)-adic numbers).

## Proof

Over \(\mathbb R\), take \(N_i=i\), \(d_j=j\), and the positive real square
root

\[
s_{ij}=\sqrt{4i+j^2}.
\]

Now let \(p\) be odd.  Take

\[
N_i=pi,\qquad d_j=1+pj.
\]

These are positive rational integers and are pairwise distinct.  Moreover,

\[
4N_i+d_j^2
=1+p(4i+2j+pj^2)\in 1+p\mathbb Z_p.
\]

Every element \(u\in1+p\mathbb Z_p\) is a square in \(\mathbb Z_p\):
apply Hensel's lemma to \(f(X)=X^2-u\) at \(X=1\), where
\(f(1)\equiv0\pmod p\) and \(f'(1)=2\not\equiv0\pmod p\).  Choose either
square root as \(s_{ij}\).

For \(p=2\), take

\[
N_i=2i,\qquad d_j=2j-1.
\]

Then

\[
4N_i+d_j^2=8i+(2j-1)^2\equiv1\pmod 8.
\]

The square units of \(\mathbb Z_2\) are exactly the units congruent to
\(1\pmod8\), so every displayed right-hand side has a square root in
\(\mathbb Z_2\).  Again all \(N_i\) and all \(d_j\) are pairwise distinct.
\(\square\)

## Consequence and scope

This rules out a real or \(p\)-adic obstruction to the grid equations on the
nondegenerate locus, for every \(k\), in particular \(k=5,6\).  It is only a
local statement.  It supplies neither integral points nor a local--global
principle.

Distinct rational integers are allowed to have the same residue modulo
\(p\).  Thus a congruence search that requires the \(N_i\), or the \(d_j\),
to occupy distinct residue classes is not a valid obstruction test.
