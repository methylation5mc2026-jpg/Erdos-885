# Family B: identities in one common parameter

All identities below are over \(\mathbb Q(t)\).  They are simultaneous
identities in one parameter, not identities in separated row and column
parameters.

## 1. A polynomial \(2\times2\) identity

Set

\[
\begin{aligned}
d_1&=4t,&d_2&=12t,\\
N_1&=t^4-20t^2+64,&
N_2&=4t^4-20t^2+16,
\end{aligned}
\]

and

\[
(s_{ij})=
\begin{pmatrix}
2t^2-16&2t^2+16\\
4t^2-8&4t^2+8
\end{pmatrix}.
\]

Direct expansion gives the four identities

\[
s_{ij}^2=4N_i+d_j^2\qquad(1\leq i,j\leq2).
\]

For every integer \(t\geq5\), both \(N_i\) are positive and

\[
N_2-N_1=3(t^4-16)>0.
\]

Thus this is already an integral, non-homothetic family proving the
\(k=2\) case.  For example, its scale-free invariant
\((N_2-N_1)/d_1^2=3(t^4-16)/(16t^2)\) is nonconstant.

The construction is the rational parametrization of
\(w^2-z^2=3^2-1^2=8\), followed by multiplication by \(4t\), using
hyperbola parameters \(t\) and \(2t\) for the two rows.

## 2. A non-homothetic rational \(3\times3\) identity

Define three auxiliary linear polynomials

\[
x=8t-30,\qquad y=10t-24,\qquad z=6t-40
\]

and their second common square translate

\[
h=\frac{(x^2y^2+x^2z^2+y^2z^2)^2}
        {4x^2y^2z^2}-(x^2+y^2+z^2).
\]

The three differences are

\[
\begin{aligned}
d_1&=\frac{x^2y^2+x^2z^2-y^2z^2}{2xyz},\\
d_2&=\frac{x^2y^2+y^2z^2-x^2z^2}{2xyz},\\
d_3&=\frac{x^2z^2+y^2z^2-x^2y^2}{2xyz}.
\end{aligned}
\]

By the common-translate lemma,

\[
d_1^2=x^2+h,\qquad d_2^2=y^2+h,\qquad d_3^2=z^2+h.
\]

Put

\[
\begin{aligned}
A_1&=0,\\
A_2&=960t,\\
A_3&=(t+12)(t-6)(t-4)(t-2),
\end{aligned}
\qquad
N_i=\frac{A_i-h}{4},
\]

and

\[
\boxed{
(s_{ij})=
\begin{pmatrix}
8t-30&10t-24&6t-40\\
8t+30&10t+24&6t+40\\
t^2-18&t^2&t^2-32
\end{pmatrix}.}
\]

Then

\[
\boxed{\qquad s_{ij}^2=4N_i+d_j^2
\quad(1\leq i,j\leq3).\qquad}
\]

### Verification

Before translation, the same matrix satisfies

\[
s_{i1}^2=A_i+x^2,\qquad
s_{i2}^2=A_i+y^2,\qquad
s_{i3}^2=A_i+z^2.
\]

For row \(2\), these are just

\[
\begin{aligned}
(8t-30)^2+960t&=(8t+30)^2,\\
(10t-24)^2+960t&=(10t+24)^2,\\
(6t-40)^2+960t&=(6t+40)^2.
\end{aligned}
\]

For row \(3\), they are

\[
\begin{aligned}
A_3+(8t-30)^2&=(t^2-18)^2,\\
A_3+(10t-24)^2&=t^4,\\
A_3+(6t-40)^2&=(t^2-32)^2.
\end{aligned}
\]

Replacing \(A_i\) by \(A_i-h=4N_i\) and replacing
\((x^2,y^2,z^2)\) by \((x^2+h,y^2+h,z^2+h)\) leaves all nine sums
unchanged, proving the boxed grid identity.

This family is not a scaling of a fixed grid, since

\[
\frac{N_2-N_1}{N_3-N_1}
=\frac{960t}{(t+12)(t-6)(t-4)(t-2)}
\]

is nonconstant.

### Positive integral specializations

For integer \(t\geq17\), \(x,y,z>0\), and the three numbers

\[
xy,\quad xz,\quad yz
\]

are the sides of a nondegenerate triangle.  The only non-immediate
triangle inequality reduces to

\[
-xy+xz+yz=4(7t^2-138t+360)>0;
\]

the other two are already positive for \(t\geq17\).  Heron's identity
therefore gives

\[
h=-\frac{(xy+xz+yz)(-xy+xz+yz)(xy-xz+yz)(xy+xz-yz)}
         {4x^2y^2z^2}<0.
\]

Consequently \(N_1>0\), and

\[
4(N_2-N_1)=960t>0,\qquad
4(N_3-N_2)=(t-12)(t+6)(t+4)(t+2)>0.
\]

Thus \(0<N_1<N_2<N_3\).  The squared differences are distinct whenever
\(x^2,y^2,z^2\) are distinct; for example this holds at \(t=17\), where
\((x,y,z)=(106,146,62)\).  At any rational specialization avoiding the
displayed denominators, homogeneity clears denominators.  More
concretely, at \(t=17\), multiplying all \(s_{ij},d_j\) by

\[
L=2xyz=1\,919\,024
\]

and all \(N_i\) by \(L^2\) gives positive integers with three distinct
positive common differences.

### Source of the formulas

Euler's semi-magic square identity, specialized at
\((p,q,r,s)=(t,3,4,5)\), gives the unshifted table above:

\[
\begin{aligned}
A_1&=0,&
A_2&=16pqrs,&
A_3&=(p+q+r+s)(p+q-r-s)(p-q+r-s)(p-q-r+s),\\
x&=2(pr-qs),&
y&=2(ps-qr),&
z&=2(pq-rs).
\end{aligned}
\]

The zero first row value would give \(N_1=0\).  The explicit second
translate \(h\) moves all three column squares by \(+h\) and all row
values by \(-h\), removing that degeneracy without changing any entry
of the square table.

## 3. Why this does not extend uniformly by the same step

For fixed distinct \(c_1,\ldots,c_m\), the smooth common-translate curve

\[
Y_j^2=X+c_j\qquad(1\leq j\leq m)
\]

has genus

\[
g=1+2^{m-2}(m-3).
\]

The proof is in `lemmas/common_translate_curve_genus.md`.  The genera for
\(m=2,3,4\) are \(0,1,5\), respectively.

For three squares, the initial translate \(X=0\) gives a point on an
elliptic curve, and duplication produces the explicit rational second
translate used above.  At four squares the curve itself has genus \(5\);
there is no curve group law and no nonconstant rational parametrization
of a fixed generic fiber.  More generally, a nonconstant family with
fixed \(c_j\)'s would induce a forbidden nonconstant map
\(\mathbb P^1\to C_m\) for every \(m\geq3\).

This is a precise obstruction to the **fixed-difference/common-translate
mechanism**, not to all common-parameter identities.  A uniform
construction for every \(k\) was not found, and these \(k=2,3\)
identities do not solve Erdős 885.
