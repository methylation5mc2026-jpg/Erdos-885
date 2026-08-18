# Rank-one multiplicative ansatz collapses

Throughout, entries and parameters are positive rational numbers. This is
enough for the integer problem because clearing denominators preserves the
grid conditions.

## Lemma 1 (one factor has rank one)

Suppose

\[
u_{ij}v_{ij}=N_i,\qquad v_{ij}-u_{ij}=d_j,
\]

and \(u_{ij}=x_i y_j\). If two of the \(d_j\)'s are distinct, then all
the \(N_i\)'s are equal.

### Proof

Put \(A_i=N_i/x_i\). Then \(v_{ij}=A_i/y_j\), so

\[
A_i-x_i y_j^2=d_jy_j.
\]

For any two rows \(i,h\),

\[
A_i-A_h=(x_i-x_h)y_j^2                                      \tag{1}
\]

for every \(j\). If all the \(y_j\)'s are equal, then every column of
\((u_{ij},v_{ij})\), and hence every \(d_j\), is equal. Thus distinct
column differences give two columns with different \(y_j^2\). Applying
(1) to those columns gives \(x_i=x_h\), then \(A_i=A_h\), and finally
\(N_i=x_iA_i=x_hA_h=N_h\). This holds for every pair of rows. \(\square\)

## Lemma 2 (both factor matrices have rank one)

Suppose instead that

\[
u_{ij}=x_i y_j,\qquad v_{ij}=z_i w_j.
\]

Then a table with at least two distinct row products and at least two
distinct positive column differences is impossible.

### Proof

Row constancy of \(u_{ij}v_{ij}\) says that \(y_jw_j=C\) is independent
of \(j\). Hence

\[
d_j=\frac{Cz_i}{y_j}-x_i y_j .
\]

Comparing rows \(i,h\) and multiplying by \(y_j\) gives

\[
C(z_i-z_h)=(x_i-x_h)y_j^2.                                  \tag{2}
\]

If all \(y_j\)'s are equal, the columns coincide. Otherwise two
different positive \(y_j\)'s in (2) force \(x_i=x_h\) and \(z_i=z_h\).
The corresponding row products \(Cx_iz_i\) are therefore equal.
\(\square\)

The reciprocal variant

\[
u_{ij}=x_i/y_j,\qquad v_{ij}=z_i y_j
\]

is the same lemma after replacing \(y_j\) by \(1/y_j\).

## Lemma 3 (rank-one centered matrix)

Let \(s_{ij}=u_{ij}+v_{ij}\), so that

\[
s_{ij}^2-d_j^2=4N_i.
\]

If \(s_{ij}=a_i b_j\), then either all positive \(d_j\)'s are equal or
all \(N_i\)'s are equal.

### Proof

For two rows \(i,h\),

\[
(a_i^2-a_h^2)b_j^2=4(N_i-N_h)
\]

for every \(j\). Two distinct values of \(b_j^2\) force
\(a_i^2=a_h^2\) and \(N_i=N_h\). If all \(b_j^2\) are equal, then
\(d_j^2=a_i^2b_j^2-4N_i\) is independent of \(j\); positivity makes
all \(d_j\) equal. \(\square\)

These lemmas rule out the literal rank-one and reciprocal-rank-one
separations. They do not rule out rank two; the two-column construction
in `lemmas/two_column_divisor_construction.md` is a non-collapsing
rank-two example.
