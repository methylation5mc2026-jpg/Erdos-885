# Family A: elliptic-curve slices for common factor differences

This note is a reconstruction, not a transcription of either paper and not a
claim of a proof for general \(k\).

## 1. Source-recovery status

The two requested records were located:

- J. Jiménez-Urroz, *A Note on a Conjecture of Erdős and Rosenfeld*,
  J. Number Theory 78 (1999), 140–143,
  [doi:10.1006/jnth.1999.2407](https://doi.org/10.1006/jnth.1999.2407).
- A. Bremner, *On a problem of Erdös related to common factor differences*,
  Int. J. Number Theory 15 (2019), 1059–1068,
  [doi:10.1142/S1793042119500581](https://doi.org/10.1142/S1793042119500581).

No valid PDF was recovered on 2026-08-18. The DOI resolver rejected automated
content negotiation. ScienceDirect returned an anti-bot page rather than a
PDF; Elsevier's metadata API labels the 1999 item `openaccessArticle=true` and
`openArchiveArticle=true`, but returns full text only with an API key.
World Scientific's official page labels the 2019 item “No Access” and offers
paid access. OpenAlex and Semantic Scholar expose no repository copy.

The zbMATH reviews confirm the following theorem statements:

- Jiménez-Urroz: for every positive integer \(r\), there is an \(r\)-element
  set \(K\) of positive integers with
  \[
  \left|\bigcap_{n\in K}D(n)\right|\geq 3.
  \]
- Bremner: there are infinitely many sets of four integers with four common
  factor differences.

Consequently, paper-specific parametrizations below are not quoted as if the
PDF had been read. What follows is an independent elliptic-slice derivation
that recovers the 1999 theorem, the generic geometry for three and four fixed
differences, and a verified \(k=4\) example indexed with the Bremner record.

## 2. Fixed-difference curve

The elementary criterion
\[
d\in D(N)\quad\Longleftrightarrow\quad 4N+d^2=s^2
\]
puts \(m\) fixed differences \(d_1,\ldots,d_m\) on the curve
\[
C_{\mathbf d}:\qquad y_j^2=x+d_j^2\quad(1\leq j\leq m),       \tag{2.1}
\]
where \(x=4N\). We always mean the smooth projective normalization of
(2.1).

Assume that the \(d_j^2\) are distinct. The map
\(C_{\mathbf d}\to\mathbf P^1_x\) has degree \(2^m\). Its branch values are
\(-d_1^2,\ldots,-d_m^2,\infty\). Above each branch value there are
\(2^{m-1}\) points of ramification index \(2\). Riemann–Hurwitz gives
\[
\begin{aligned}
2g(C_{\mathbf d})-2
  &=-2\cdot2^m+(m+1)2^{m-1}\\
  &=2^{m-1}(m-3),
\end{aligned}
\]
hence
\[
\boxed{g(C_{\mathbf d})=1+2^{m-2}(m-3).}                    \tag{2.2}
\]
In particular:
\[
m=2:\ g=0,\qquad m=3:\ g=1,\qquad
m=4:\ g=5,\qquad m=5:\ g=17.                               \tag{2.3}
\]

Thus three fixed differences genuinely give an elliptic curve. Four generic
fixed differences do **not** have one Weierstrass model: their simultaneous
curve has genus \(5\).

## 3. Three fixed differences: a birational Weierstrass model

Put
\[
A=d_2^2-d_1^2,\qquad B=d_3^2-d_1^2.
\]
Writing \(z=y_1,\ u=y_2,\ v=y_3\), eliminate \(x\):
\[
u^2-z^2=A,\qquad v^2-z^2=B.                                \tag{3.1}
\]
Parametrize the first conic by
\[
t=u+z,\qquad
z=\frac{t^2-A}{2t},\qquad u=\frac{t^2+A}{2t}.
\]
If \(q=2tv\), the remaining equation is the Jacobi quartic
\[
q^2=t^4+(4B-2A)t^2+A^2.                                   \tag{3.2}
\]
Set \(c=4B-2A\). A direct birational transformation is
\[
X=c+\frac{2A(q+A)}{t^2},\qquad Y=\frac{2AX}{t}.             \tag{3.3}
\]
It gives the Weierstrass equation
\[
\boxed{E_{A,B}:\quad
Y^2=X\bigl(X-4B\bigr)\bigl(X-4(B-A)\bigr).}                 \tag{3.4}
\]
Away from finitely many exceptional points, the inverse is
\[
t=\frac{2AX}{Y},\qquad
q=\frac{(X-c)t^2}{2A}-A,                                   \tag{3.5}
\]
followed by the formulas above and \(v=q/(2t)\). Finally
\[
x=z^2-d_1^2,\qquad N=x/4.                                  \tag{3.6}
\]
The discriminant of (3.4) is
\[
\Delta=2^{16}A^2B^2(B-A)^2,
\]
so distinct \(d_i^2\) give a nonsingular curve.

### A compact positive-rank instance

Take
\[
(d_1,d_2,d_3)=(6,54,111),\qquad
(A,B)=(2880,12285).
\]
Then
\[
\boxed{E:\quad
Y^2=X(X-49140)(X-37620)
   =X^3-86760X^2+1848646800X.}                              \tag{3.7}
\]
The following three points arise from (3.3):
\[
\begin{array}{c|c|c}
N&(z,u,v)&(X,Y)\\ \hline
112 &(22,58,113)&(62244,4481568)\\
952 &(62,82,127)&(54340,2173600)\\
3240&(114,126,159)&(51300,1231200).
\end{array}                                                 \tag{3.8}
\]
The first point in (3.8) is non-torsion. One short certificate is reduction
modulo \(43\): the curve has good reduction there and the reduced point has
order \(28\). If the rational point were torsion, its reduced order would
divide its rational torsion order, but Mazur's list has maximum torsion-group
order \(16\).

It follows that (3.7), and hence (3.1), has infinitely many rational points.
The rational function \(N\) in (3.6) has finite fibers. Multiples of a
non-torsion real point approach the points at infinity, where \(N>0\), so
infinitely many distinct positive rational \(N\)'s occur. Given any finite
number \(r\) of them, one common scaling clears all denominators:
\[
(N,d,y)\longmapsto(\lambda^2N,\lambda d,\lambda y).
\]
Taking \(\lambda\) sufficiently divisible also makes every
\(\lambda^2N\) integral. This independently reconstructs the theorem
attributed to Jiménez-Urroz: arbitrarily many integers can share three
positive differences. It does not purport to reproduce his particular
choice of curve.

## 4. Four fixed differences: genus five and five elliptic quotients

Let \(a_i=d_i^2\). The sign changes of the four square roots in (2.1) give an
action of \((\mathbf Z/2\mathbf Z)^4\). For each subset \(S\), multiplication
of the corresponding square roots gives a quotient
\[
H_S:\qquad w_S^2=\prod_{i\in S}(x+a_i).                    \tag{4.1}
\]
For \(|S|=3\) or \(4\), this quotient has genus \(1\). Thus a generic
four-difference curve has five elliptic quotients: four cubics and one
quartic. Character decomposition gives, up to isogeny,
\[
\operatorname{Jac}(C_{\mathbf d})
\sim
\prod_{|S|=3}H_S\ \times H_{\{1,2,3,4\}},                  \tag{4.2}
\]
whose dimensions \(4+1\) account for genus \(5\).

The four cubic Weierstrass equations are already explicit. For example, if
\[
t=x+a_i,\quad A=a_j-a_i,\quad B=a_k-a_i,
\]
then
\[
w^2=t(t+A)(t+B).                                           \tag{4.3}
\]

For the four-element quotient, put
\[
A=a_2-a_1,\quad B=a_3-a_1,\quad C=a_4-a_1,\quad t=x+a_1.
\]
Starting from
\[
w^2=t(t+A)(t+B)(t+C),                                     \tag{4.4}
\]
the substitution
\[
U=\frac{ABC}{t},\qquad V=\frac{ABC\,w}{t^2}
\]
gives the monic Weierstrass equation
\[
\boxed{
V^2=U^3+(AB+AC+BC)U^2+(A+B+C)ABC\,U+(ABC)^2.}              \tag{4.5}
\]

Equations (4.3)–(4.5) are quotient curves, not a replacement for all four
simultaneous square conditions. A rational point on one quotient need not
lift to \(C_{\mathbf d}\). This is the precise reason that merely displaying
an elliptic quotient does not prove the four-difference result.

## 5. Explicit examples

### \(k=3\)

\[
\boxed{\{6,54,111\}\subset
D(112)\cap D(952)\cap D(3240).}
\]
The factor pairs are
\[
\begin{array}{c|ccc}
N&d=6&d=54&d=111\\ \hline
112 &(8,14)&(2,56)&(1,112)\\
952 &(28,34)&(14,68)&(8,119)\\
3240&(54,60)&(36,90)&(24,135).
\end{array}
\]

### \(k=4\), beyond Guiduli's three-row examples

Web indexing associated the following example with the Bremner record; the
PDF itself was unavailable. It has been independently verified by exhaustive
divisor enumeration:
\[
\boxed{
\begin{aligned}
D(26128575)&\cap D(291722431)\\
&\cap D(561117375)\cap D(713526975)\\
&=\{126,16110,33390,75390\}.
\end{aligned}}                                             \tag{5.1}
\]
Factor-pair witnesses are
\[
\begin{array}{c|rrrr}
N&126&16110&33390&75390\\ \hline
26128575 &(5049,5175)&(1485,17595)&(765,34155)&(345,75735)\\
291722431&(17017,17143)&(10829,26939)&(7189,40579)&(3689,79079)\\
561117375&(23625,23751)&(16965,33075)&(12285,45675)&(6825,82215)\\
713526975&(26649,26775)&(19845,35955)&(14805,48195)&(8505,83895).
\end{array}                                                 \tag{5.2}
\]

For these four differences, set \(x=4N\). The genus-five curve is
\[
\begin{cases}
y_1^2=x+15876,\\
y_2^2=x+259532100,\\
y_3^2=x+1114892100,\\
y_4^2=x+5683652100.
\end{cases}                                                 \tag{5.3}
\]
Its four displayed integral points have
\[
\begin{array}{c|rrrr}
x&y_1&y_2&y_3&y_4\\ \hline
104514300 &10224&19080&34920&76080\\
1166889724&34160&37768&47768&82768\\
2244469500&47376&50040&57960&89040\\
2854107900&53424&55800&63000&92400.
\end{array}                                                 \tag{5.4}
\]

For reference, the all-four elliptic quotient (4.4) is
\[
\begin{aligned}
w^2={}&t(t+259516224)(t+1114876224)\\
     &\qquad\cdot(t+5683636224).                            \tag{5.5}
\end{aligned}
\]
Its Weierstrass form (4.5) is
\[
\begin{aligned}
V^2={}&U^3+8100875171324694528\,U^2\\
&+11606488864173381156637183283904380928\,U\\
&+2704175548738355147892503529949795668834137005438795776.
\end{aligned}                                               \tag{5.6}
\]

The verified example (5.1) proves \(k=4\) by itself. The stronger statement
that infinitely many such quadruples exist is Bremner's published theorem,
but the unavailable body of the paper prevents an honest reconstruction of
his specific parameter, elliptic curve, generator, and specialization
argument.

## 6. The five-difference obstruction

For five distinct fixed differences, (2.2) gives
\[
g(C_{d_1,\ldots,d_5})=17.
\]
Equivalently, adding \(y_5^2=x+d_5^2\) to the genus-five
four-difference curve is generically a double cover ramified at the sixteen
points above \(x=-d_5^2\). Riemann–Hurwitz gives
\[
2g_5-2=2(2g_4-2)+16=32,
\]
again yielding \(g_5=17\).

Faltings therefore implies that a fixed generic five-difference slice has
only finitely many rational \(x\)-values. This is a precise obstruction to
the Jiménez-Urroz strategy “positive Mordell–Weil rank gives arbitrarily many
rows with the same fixed differences.”

Two qualifications are essential:

1. Generic four-difference slices already have genus \(5\); Bremner's theorem
   must use a special moving locus or other algebraic dependence, rather than
   generic fixed differences.
2. Faltings gives finiteness, not a bound below five. A genus-\(17\) curve can
   have five or more rational points. Thus this is not a disproof of \(k=5\).

If a four-row construction is parametrized by an elliptic curve \(E\), a
fifth square condition normally has the form
\[
W^2=f(P),\qquad P\in E.
\]
This is a double cover of \(E\). If the divisor of \(f\) has \(r\) odd-order
zeros and poles, Riemann–Hurwitz gives genus \(1+r/2\); generically \(r>0\),
so the new curve has genus greater than \(1\). To remain elliptic, one must
prove a special even-divisor or unramified condition and then prove positive
rank. No such lemma follows from the sentence “the ideas of this paper can
be extended.” The abstract and reviews state only \(k=4\), and contain no
quantified \(k=5\) theorem.

## 7. Exact missing lemma for general \(k\)

The fixed-slice route is missing the following statement.

> **Missing slice lemma.** For every \(k\geq1\), there are pairwise distinct
> positive rationals \(d_1,\ldots,d_k\) for which the curve
> \[
> C_{\mathbf d}: y_j^2=x+d_j^2\quad(1\leq j\leq k)
> \]
> has at least \(k\) affine rational points with pairwise distinct positive
> \(x\)-coordinates.

This lemma is sufficient: choose one common \(\lambda\) clearing all
denominators and making every \(\lambda^2x_i\) divisible by \(4\); then
\[
N_i=\lambda^2x_i/4,\qquad d'_j=\lambda d_j
\]
are integers and \(d'_j\in D(N_i)\) for every \(i,j\).

It is also essentially equivalent to the original conjecture after rational
scaling, so merely restating it is not progress. A useful elliptic-family
replacement would have to supply, for every \(k\), a special locus on which
the \(k\) square conditions become algebraically dependent, together with:

1. an explicit genus-zero or genus-one parameter curve;
2. a rational point of infinite order when the curve is elliptic;
3. \(k\) distinct positive rows and \(k\) distinct positive differences at
   infinitely many specializations; and
4. one simultaneous denominator-clearing argument.

Jiménez-Urroz supplies this mechanism for three differences and Bremner for
four rows/four differences. No such dependence or rank lemma is presently
available here for five differences, let alone uniformly for all \(k\).
