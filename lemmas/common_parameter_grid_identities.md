# Common-parameter square-grid identities for \(k=2,3\)

## Proposition

There are non-homothetic one-parameter families over \(\mathbb Q(t)\)
satisfying

\[
s_{ij}(t)^2=4N_i(t)+d_j(t)^2
\]

for \(k=2\) and for \(k=3\).

### The \(2\times2\) family

\[
\begin{gathered}
(d_1,d_2)=(4t,12t),\\
(N_1,N_2)=(t^4-20t^2+64,\;4t^4-20t^2+16),\\
(s_{ij})=
\begin{pmatrix}
2t^2-16&2t^2+16\\
4t^2-8&4t^2+8
\end{pmatrix}.
\end{gathered}
\]

All four equations follow by expansion.

### The \(3\times3\) family

Let

\[
x=8t-30,\qquad y=10t-24,\qquad z=6t-40
\]

and define

\[
\begin{aligned}
h&=\frac{(x^2y^2+x^2z^2+y^2z^2)^2}{4x^2y^2z^2}
 -(x^2+y^2+z^2),\\
d_1&=\frac{x^2y^2+x^2z^2-y^2z^2}{2xyz},\\
d_2&=\frac{x^2y^2+y^2z^2-x^2z^2}{2xyz},\\
d_3&=\frac{x^2z^2+y^2z^2-x^2y^2}{2xyz}.
\end{aligned}
\]

Set

\[
(A_1,A_2,A_3)=
\left(0,\;960t,\;(t+12)(t-6)(t-4)(t-2)\right),
\qquad N_i=\frac{A_i-h}{4},
\]

and

\[
(s_{ij})=
\begin{pmatrix}
8t-30&10t-24&6t-40\\
8t+30&10t+24&6t+40\\
t^2-18&t^2&t^2-32
\end{pmatrix}.
\]

Then all nine grid equations hold.

## Proof for \(k=3\)

The second-translate identities proved in
`lemmas/common_translate_curve_genus.md` give

\[
(d_1^2,d_2^2,d_3^2)=(x^2+h,y^2+h,z^2+h).
\]

Direct expansion gives

\[
s_{ij}^2=A_i+(x^2,y^2,z^2)_j.
\]

Therefore

\[
s_{ij}^2
=A_i+(x^2,y^2,z^2)_j
=(A_i-h)+(d_1^2,d_2^2,d_3^2)_j
=4N_i+d_j^2.
\]

The ratio

\[
\frac{N_2-N_1}{N_3-N_1}
=\frac{960t}{(t+12)(t-6)(t-4)(t-2)}
\]

is nonconstant, so the family is not merely a homothetic copy of one
fixed numerical grid.  Positivity, ordering, and denominator clearing
are detailed in `research/family_B_identities.md`. \(\square\)
