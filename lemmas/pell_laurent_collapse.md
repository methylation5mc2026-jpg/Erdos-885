# Collapse of the two-term Pell-unit ansatz

The standard use of a norm-one unit writes its two embeddings as
\(t\) and \(t^{-1}\). Traces of products with fixed ring elements
therefore have the Laurent form \(At+B/t\). The following lemma tests
exactly that ansatz.

## Lemma

Let \(F\) be a field of characteristic different from \(2\). Fix
\(C,D\in F\), and let \(t_1,t_2,t_3\in F^\times\) have pairwise
distinct squares. For each row \(i\), choose \(A_i,B_i,N_i\in F\).
Suppose

\[
\left(A_it_j+\frac{B_i}{t_j}\right)^2
-
\left(Ct_j+\frac{D}{t_j}\right)^2
=4N_i                                                     \tag{1}
\]

for \(j=1,2,3\). Then

\[
A_i^2=C^2,\qquad B_i^2=D^2,
\]

and \(N_i\) is either \(0\) or \(-CD\). In particular, over an ordered
field, all positive row products occurring in (1) are equal.

### Proof

Set \(z=t_j^2\), expand (1), and multiply by \(z\). Each of the three
distinct values \(z=t_j^2\) is a root of

\[
(A_i^2-C^2)z^2+
\bigl(2(A_iB_i-CD)-4N_i\bigr)z+
(B_i^2-D^2).
\]

This polynomial has degree at most two, so all three coefficients
vanish. Thus \(A_i=\pm C\), \(B_i=\pm D\), and

\[
N_i=\frac{A_iB_i-CD}{2}.
\]

If the two signs have the same product, this is \(0\); if they have
opposite product, it is \(-CD\). \(\square\)

## Pell-unit interpretation

For a real quadratic norm-one unit \(\varepsilon\), take
\(t_j=\varepsilon^{n_j}\) in one real embedding; the conjugate is
\(t_j^{-1}\). Thus three distinct unit powers in the natural
trace/anti-trace construction cannot produce both three columns and
distinct positive row products.

There is also a direct norm mismatch. If

\[
x_n+y_n\sqrt{\Delta}=\alpha\varepsilon^n,\qquad
x_n^2-\Delta y_n^2=C
\]

with nonsquare \(\Delta>1\), assigning \(s=x_n\) and \(d=y_n\) gives

\[
s^2-d^2=C+(\Delta-1)y_n^2,
\]

which is not constant along a nontrivial Pell orbit. Assigning
\(d=\sqrt{\Delta}\,y_n\) would repair the norm but generally makes the
required factor difference irrational. This is an obstruction to the
standard Pell encoding, not a theorem excluding every construction
that happens to use Pell numbers.
