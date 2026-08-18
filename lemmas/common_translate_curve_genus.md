# Common translates of squares

## Explicit second translate for three squares

Let \(x,y,z\) be nonzero elements of a field of characteristic different
from \(2\).  Put

\[
\begin{aligned}
e_x&=\frac{x^2y^2+x^2z^2-y^2z^2}{2xyz},\\
e_y&=\frac{x^2y^2+y^2z^2-x^2z^2}{2xyz},\\
e_z&=\frac{x^2z^2+y^2z^2-x^2y^2}{2xyz},
\end{aligned}
\]

and

\[
h=\frac{(x^2y^2+x^2z^2+y^2z^2)^2}
        {4x^2y^2z^2}-(x^2+y^2+z^2).
\]

Then

\[
e_x^2=x^2+h,\qquad e_y^2=y^2+h,\qquad e_z^2=z^2+h.
\]

Indeed, for the first identity,

\[
(x^2y^2+x^2z^2-y^2z^2)^2
=(x^2y^2+x^2z^2+y^2z^2)^2
-4x^2y^2z^2(y^2+z^2),
\]

and division by \(4x^2y^2z^2\) gives \(e_x^2=x^2+h\).
The other two identities follow by permutation.  This is a rational
second common translate of the three initial squares.  It is nontrivial
unless the displayed rational function \(h\) vanishes.

Equivalently, on

\[
E:\quad Y^2=(X+x^2)(X+y^2)(X+z^2),
\]

the point \(P=(0,xyz)\) has

\[
X(2P)=h.
\]

The three displayed square roots are the corresponding elementary
\(2\)-descent identities.

## Genus obstruction for a fixed list

Let \(K\) be a field of characteristic \(0\), let \(m\geq2\), and let
\(c_1,\ldots,c_m\in K\) be pairwise distinct.  Let \(C_m\) be the smooth
projective curve with function field

\[
K(C_m)=K(X)\bigl(\sqrt{X+c_1},\ldots,\sqrt{X+c_m}\bigr).
\]

Then

\[
\boxed{\quad g(C_m)=1+2^{m-2}(m-3).\quad}
\]

In particular \(g(C_2)=0\), \(g(C_3)=1\), and \(g(C_4)=5\).

### Proof

The square classes of \(X+c_1,\ldots,X+c_m\) are independent in
\(K(X)^\times/K(X)^{\times2}\): the valuation at \(X=-c_i\) detects the
\(i\)-th class.  Thus the map \(C_m\to\mathbb P^1_X\) has degree \(2^m\).
It is ramified precisely over

\[
-c_1,\ldots,-c_m,\infty.
\]

At each of these \(m+1\) points the inertia group has order \(2\), so
there are \(2^{m-1}\) points above it and its total contribution to the
different is \(2^{m-1}\).  Riemann--Hurwitz gives

\[
2g(C_m)-2=-2\cdot2^m+(m+1)2^{m-1}
          =2^{m-1}(m-3),
\]

which is the claimed formula. \(\square\)

### Exact scope of the obstruction

If \(c_1,\ldots,c_m\) are fixed and distinct, a rational-function family

\[
X=X(t),\qquad Y_j=Y_j(t),\qquad Y_j(t)^2=X(t)+c_j
\]

with nonconstant \(X(t)\) would give a nonconstant morphism
\(\mathbb P^1\to C_m\).  This is impossible for \(m\geq3\) by
Riemann--Hurwitz.  Thus fixed differences cannot yield a nonconstant
one-parameter rational identity once there are three columns.

This does **not** rule out identities in which the \(c_j\) themselves
vary with \(t\).  The \(3\times3\) identity in
`research/family_B_identities.md` does exactly that.  For \(m\geq4\),
the genus-\(\geq5\) result explains precisely why the three-square
duplication/translation step has no direct uniform analogue; it is not
a non-existence theorem for all of Erdős 885.
