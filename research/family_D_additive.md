# Family D: additive square tables and the missing square side

## Scope

Choudhry, arXiv:2508.07806, constructs integer sets \(A,B\) for which every
\(A_i+B_j\) is a square.  This is not by itself a solution of Erdős 885.
The extra condition is analyzed below, including the positivity condition
that is easy to lose when translating an additive table.

## Explicit tables from Choudhry

The paper's numerical \(5\times3\) example (Theorem 2) is

\[
\begin{aligned}
A={}&\{198916,532900,1674436,13468900,19404025\},\\
B={}&\{0,3588000,8527200\}.
\end{aligned}
\]

The matrix of nonnegative square roots of \(A_i+B_j\) is

\[
\begin{pmatrix}
446&1946&2954\\
730&2030&3010\\
1294&2294&3194\\
3670&4130&4690\\
4405&4795&5285
\end{pmatrix}.
\]

The paper gives two new numerical \(4\times4\) examples.  Theorem 3 gives

\[
\begin{aligned}
A={}&\{44782864,340218025,1738222864,2777290000\},\\
B={}&\{0,25777136,1222007600,1719217136\},
\end{aligned}
\]

with root matrix

\[
\begin{pmatrix}
6692&8400&35592&42000\\
18445&19131&39525&45381\\
41692&42000&54408&58800\\
52700&52944&63240&67056
\end{pmatrix}.
\]

Theorem 4 gives

\[
\begin{aligned}
A={}&\{14400,266256,435600,12110400\},\\
B={}&\{0,104625,223744,12096000\},
\end{aligned}
\]

with root matrix

\[
\begin{pmatrix}
120&345&488&3480\\
516&609&700&3516\\
660&735&812&3540\\
3480&3495&3512&4920
\end{pmatrix}.
\]

For completeness, section 1 also quotes the older Lagrange example

\[
A=\{324,54756,119716,264196\},\qquad
B=\{0,79200,227205,1258560\},
\]

whose root matrix is

\[
\begin{pmatrix}
18&282&477&1122\\
234&366&531&1146\\
346&446&589&1174\\
514&586&701&1234
\end{pmatrix}.
\]

Machine-readable copies are in
`examples/choudhry_additive_tables.json`.

## What “a translate of squares” must mean

Suppose the table is normalized by \(B_1=0\):

\[
S_{ij}^2=A_i+B_j.
\]

Scaling by \(q^2\) and translating the two sides in opposite directions gives

\[
q^2A_i-x^2,\qquad q^2B_j+x^2.
\]

Thus the square-side equations are

\[
y_j^2=x^2+q^2B_j. \tag{1}
\]

Scaling does not remove this condition: after division by \(q^2\), it says
that the rational translate \(B_j+(x/q)^2\) consists of rational squares.
But (1) alone is not enough for Erdős 885.  Positive row integers require

\[
0<x^2<q^2\min_i A_i. \tag{2}
\]

When (1) and (2) hold with integers \(q,x,y_j\), set

\[
N_i=q^2A_i-x^2,\qquad d_j=2y_j,\qquad
s'_{ij}=2qS_{ij}.
\]

Then all \(N_i\) are positive and

\[
(s'_{ij})^2=4N_i+d_j^2.
\]

This also explains a trap.  For every row \(r\), taking
\(q=1,\ x=S_{r1}\), and \(y_j=S_{rj}\) makes (1) true.  In particular,
\(B+A_r\) is automatically a set of squares for every additive square
table.  If \(A_r=\min A\), however, one transformed row is zero; if
\(A_r>\min A\), some transformed rows are negative.  Such automatic
translates do not solve 885.

For the examples above, \(B\) itself is not a set of squares.  Their smallest
row gives these automatic boundary translates:

| example | \(t=\min A\) | roots of \(B+t\) | obstruction |
|---|---:|---|---|
| Choudhry \(5\times3\) | 198916 | \(446,1946,2954\) | one \(A_i-t=0\) |
| Choudhry Theorem 3 \(4\times4\) | 44782864 | \(6692,8400,35592,42000\) | one \(A_i-t=0\) |
| Choudhry Theorem 4 \(4\times4\) | 14400 | \(120,345,488,3480\) | one \(A_i-t=0\) |
| cited Lagrange \(4\times4\) | 324 | \(18,282,477,1122\) | one \(A_i-t=0\) |

An exact factor-pair search found no admissible translate satisfying (1)-(2)
for any of these tables when the reduced denominator obeys
\(1\le q\le20000\).  This is a bounded negative result, not a proof that no
rational translate exists.  It is reproduced by

```text
python3 compute/check_choudhry_tables.py --denominator-bound 20000
```

For each \(q\), factor pairs of \(q^2B_2\) exhaust all possible \(x\) in the
first equation \(y_2^2-x^2=q^2B_2\); the remaining equations and (2) are then
checked exactly.

## Exact remaining condition for \(k=5\)

For a normalized unrestricted \(5\times5\) table with
\(B_1=0\), the missing Diophantine condition is exactly

\[
\boxed{
\begin{aligned}
y_2^2-x^2&=q^2B_2,\\
y_3^2-x^2&=q^2B_3,\\
y_4^2-x^2&=q^2B_4,\\
y_5^2-x^2&=q^2B_5,\\
0&<x^2<q^2\min_{1\le i\le5}A_i,
\end{aligned}}
\tag{3}
\]

in integers \(q>0,x,y_2,y_3,y_4,y_5\), with \(y_1=x\).  Equivalently,
there must be a rational \(T\), strictly between \(0\) and \(\min A\), such
that all five \(B_j+T\) are rational squares.  Clearing denominators in this
rational statement gives (3).  Distinct \(B_j\) give distinct positive
differences.

Without the strict inequality in (3), every row of the starting table gives
a tautological solution of the four equations and no progress on 885.

## Bounded \(5\times5\) searches

The exact finite search in `compute/search_additive_tables.py` uses the
incidence relation

\[
v^2-u^2=c,\qquad 1\le u<v\le R.
\]

For unrestricted tables, a \(K_{5,4}\) in this incidence graph gives five
positive first-column roots \(u_i\), four positive offsets \(c_j\), and the
fifth offset \(0\).  For square-side tables, a \(K_{5,5}\) is reinterpreted
as five positive differences \(d_j=u_j\) and five positive row constants
\(A_i=c_i\).

With \(R=2000\), there are 990682 distinct positive labels \(c\), of which
75122 have support at least five.  Exhaustive frequent-itemset searches gave:

* no unrestricted \(5\times5\) table with \(B_1=0\), \(B_j>0\), and every
  cell root in \([1,2000]\);
* no \(5\times5\) square-side table with \(A_i>0\), \(d_j>0\), and every
  \(d_j,s_{ij}\) in \([1,2000]\).

The command is

```text
python3 compute/search_additive_tables.py --bound 2000
```

These searches neither produce nor disprove a \(5\times5\) table outside
the stated boxes.  In particular, the unrestricted search is not reported
as a solution of Erdős 885.
