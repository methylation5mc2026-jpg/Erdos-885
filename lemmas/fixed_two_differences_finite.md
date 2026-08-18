# The fiber over two fixed differences is finite

## Lemma

Fix integers \(0\leq d<e\).  Every positive integer \(N\) satisfying

\[
d,e\in D(N)
\]

arises from a positive factorization

\[
uv=e^2-d^2,\qquad u<v,\qquad u\equiv v\pmod2
\]

by the formulas

\[
x=\frac{v-u}{2},\qquad N=\frac{x^2-d^2}{4},
\]

subject to \(x>d\) and \(x\equiv d\pmod2\).  Consequently there are only
finitely many such \(N\), and enumerating the divisors of \(e^2-d^2\) is
an exhaustive search.

## Proof

By the square criterion, there are positive integers \(x,y\) with

\[
x^2=4N+d^2,\qquad y^2=4N+e^2.
\]

Since \(e>d\), we have \(y>x\).  Subtraction gives

\[
(y-x)(y+x)=y^2-x^2=e^2-d^2.
\]

Put \(u=y-x\) and \(v=y+x\).  They are positive, \(u<v\), have the same
parity, and satisfy the asserted factorization.  Solving for \(x\) gives
\(x=(v-u)/2\), after which \(N=(x^2-d^2)/4\).

Conversely, every factor pair satisfying the displayed integrality and
positivity conditions gives a candidate \(N\).  Directly checking
\(4N+d^2\) and \(4N+e^2\) proves membership for the first two differences;
any further prescribed differences are then exact perfect-square tests.
There are finitely many factor pairs because \(e^2-d^2\ne0\).
\(\square\)

## Computational use

`compute/family_G_lift.py` implements precisely this divisor enumeration.
Unlike a scan up to a chosen square-root bound, it cannot miss a larger
positive integer \(N\).
