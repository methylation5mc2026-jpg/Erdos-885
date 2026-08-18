# Standard tensor compositions preserve only one grid constraint

Let

\[
u_{ij}v_{ij}=N_i,\qquad v_{ij}-u_{ij}=d_j
\]

and

\[
p_{r\ell}q_{r\ell}=M_r,\qquad
q_{r\ell}-p_{r\ell}=e_\ell
\]

be positive rational factor-difference grids.

## Lemma 1 (factor-pair Kronecker product)

Define

\[
U_{(i,r),(j,\ell)}=u_{ij}p_{r\ell},\qquad
V_{(i,r),(j,\ell)}=v_{ij}q_{r\ell}.                         \tag{1}
\]

Then \(UV=N_iM_r\), so (1) preserves constant row products. However,
if both source grids have positive column differences and distinct row
products, no composite column has a difference constant on all
composite rows.

### Proof

For a fixed composite column \((j,\ell)\),

\[
\begin{aligned}
V-U
&=(u_{ij}+d_j)(p_{r\ell}+e_\ell)-u_{ij}p_{r\ell}\\
&=e_\ell u_{ij}+d_jp_{r\ell}+d_je_\ell.                    \tag{2}
\end{aligned}
\]

If (2) were independent of \(i\), positivity of \(e_\ell\) would make
\(u_{ij}\) independent of \(i\). Then
\(N_i=u_{ij}(u_{ij}+d_j)\) would also be independent of \(i\), contrary
to distinct source row products. The same argument in \(r\) applies
to the other source grid. \(\square\)

The crossed split-norm product

\[
U=u_{ij}q_{r\ell},\qquad V=v_{ij}p_{r\ell}
\]

does not help: its oriented difference is

\[
V-U=d_jp_{r\ell}-e_\ell u_{ij},
\]

which has the same row dependence. These parallel and crossed products
are the two multiplicative pairings obtained from the identity
\((s^2-d^2)(t^2-e^2)=S^2-D^2\).

## Concrete counterexample

The valid \(2\times2\) table

\[
\begin{array}{c|cc}
N&d=2&d=26\\ \hline
1680&(40,42)&(30,56)\\
360 &(18,20)&(10,36)
\end{array}
\]

has constant products on rows and constant differences on columns.
In its parallel Kronecker square, the composite column formed from the
two \(d=2\) columns has differences

\[
164,\quad120,\quad120,\quad76
\]

on the four ordered row pairs. Thus the row-product condition survives
while the column-difference condition fails.

## Lemma 2 (square/norm tensor)

Write the grids in centered form

\[
s_{ij}^2=d_j^2+4N_i,\qquad
t_{r\ell}^2=e_\ell^2+4M_r.
\]

The tempting norm tensor

\[
S_{(i,r),(j,\ell)}=s_{ij}t_{r\ell},\qquad
D_{j\ell}=d_je_\ell
\]

does preserve a difference \(D_{j\ell}\) depending only on the
composite column, but its induced product is

\[
\frac{S^2-D^2}{4}
=d_j^2M_r+e_\ell^2N_i+4N_iM_r.                             \tag{3}
\]

Hence it is generally not constant on a composite row.

For a numerical counterexample, use

\[
\begin{array}{c|cc}
N&d=15&d=48\\ \hline
100&(5,20)&(2,50)\\
324&(12,27)&(6,54).
\end{array}
\]

Its centered entries are \((25,52)\) and \((39,60)\). In the
composite row \((100,100)\), formula (3) gives products

\[
85000\quad\text{at column }(15,15),\qquad
292900\quad\text{at column }(15,48).
\]

Thus this composition preserves the column parameter but destroys the
row constraint.

## Lemma 3 (direct block sum has no free cross blocks)

Keeping two grids as diagonal blocks produces a larger grid if and
only if every row product of either block already admits every column
difference of the other block.

### Proof

The upper-right block exists exactly when
\(e_\ell\in D(N_i)\) for every \(i,\ell\), and the lower-left block
exists exactly when \(d_j\in D(M_r)\) for every \(r,j\). These are
precisely the missing cross-incidence conditions. \(\square\)

Consequently a direct block sum merely restates the enlarged-grid
problem; it does not construct the off-diagonal blocks.
