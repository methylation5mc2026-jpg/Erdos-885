# An unbounded two-column divisor construction

## Lemma

Let \(t\ge 2\) be an integer, and put

\[
M=t(t+1),\qquad \beta=2t+1.
\]

For every proper positive divisor \(a<t\) of \(t\), define

\[
b=\frac{M}{a},\qquad x=b-a,\qquad y=b+a,\qquad N_a=x^2-1.
\]

Then the two factor pairs

\[
(u_{a1},v_{a1})=(x-1,x+1),
\]

\[
(u_{a2},v_{a2})=(y-\beta,y+\beta)
\]

are positive and have the same product \(N_a\). Their differences are
the two values

\[
d_1=2,\qquad d_2=2\beta=4t+2,
\]

independent of \(a\). The \(N_a\)'s are distinct as \(a\) ranges over
the proper divisors of \(t\).

### Proof

The first product is \(x^2-1=N_a\). The elementary split-norm identity

\[
y^2-x^2=(b+a)^2-(b-a)^2=4ab=4M=\beta^2-1
\]

gives

\[
y^2-\beta^2=x^2-1=N_a,
\]

which proves the second product identity. The displayed factor
differences are immediate.

Write \(t=ac\). Since \(a\) is proper, \(c\ge2\), and

\[
y-\beta=a(c-1)^2+c-1>0.
\]

All four factors are therefore positive. Also every such \(a\) lies in
\((0,t)\), while \(t<\sqrt{M}\). The real function
\(M/a-a\) is strictly decreasing on this interval, so the positive
values \(x\), and hence the values \(N_a=x^2-1\), are distinct.
\(\square\)

## Consequence

The construction gives \(\tau(t)-1\) distinct rows and two columns.
Taking \(t\) to be a product of \(m\) distinct primes gives
\(2^m-1\) rows. Hence, for every \(r\), there is a genuine
\(r\times2\) factor-difference grid.

This is a non-collapsing rank-two variant. Indeed, in centered
coordinates \(s=u+v\), its two columns are

\[
s_{a1}=2(b-a),\qquad s_{a2}=2(b+a),
\]

the two Hadamard combinations of \(a\) and \(M/a\). It does not add a
third column and therefore does not give square \(k\times k\) grids
for arbitrary \(k\).

For example, \(t=6\) gives \(M=42\), \(\beta=13\), and

\[
\begin{array}{c|cc}
N_a & d=2 & d=26\\ \hline
1680&(40,42)&(30,56)\\
360 &(18,20)&(10,36)\\
120 &(10,12)&(4,30).
\end{array}
\]
