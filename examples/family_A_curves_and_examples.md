# Elliptic-slice curves and verified examples

## Three fixed differences

For \((d_1,d_2,d_3)=(6,54,111)\), the simultaneous-square curve is
birational to
\[
Y^2=X(X-49140)(X-37620).
\]
The points
\[
(62244,4481568),\quad(54340,2173600),\quad(51300,1231200)
\]
correspond respectively to \(N=112,952,3240\).

Factor-pair witnesses:

```text
N=112:  (8,14), (2,56),  (1,112)   differences 6,54,111
N=952:  (28,34),(14,68), (8,119)   differences 6,54,111
N=3240: (54,60),(36,90), (24,135)  differences 6,54,111
```

The first elliptic point reduces to order \(28\) at the good prime \(43\),
so it is non-torsion.

## Four integers and four common differences

```text
N = 26128575, 291722431, 561117375, 713526975
d = 126, 16110, 33390, 75390
```

Square-root witness matrix for \(4N_i+d_j^2=s_{ij}^2\):

```text
             126    16110   33390   75390
26128575     10224  19080   34920   76080
291722431    34160  37768   47768   82768
561117375    47376  50040   57960   89040
713526975    53424  55800   63000   92400
```

Factor-pair witnesses \((a,b)\), with \(ab=N_i\) and \(b-a=d_j\):

```text
26128575:
  (5049,5175) (1485,17595) (765,34155)  (345,75735)
291722431:
  (17017,17143) (10829,26939) (7189,40579) (3689,79079)
561117375:
  (23625,23751) (16965,33075) (12285,45675) (6825,82215)
713526975:
  (26649,26775) (19845,35955) (14805,48195) (8505,83895)
```

Exhaustive divisor enumeration gives the exact intersection
\[
D(26128575)\cap D(291722431)\cap D(561117375)\cap D(713526975)
=\{126,16110,33390,75390\}.
\]

For these fixed differences, the simultaneous curve has genus \(5\):
\[
\begin{cases}
y_1^2=x+15876,\\
y_2^2=x+259532100,\\
y_3^2=x+1114892100,\\
y_4^2=x+5683652100.
\end{cases}
\]
Its all-four elliptic quotient is
\[
w^2=t(t+259516224)(t+1114876224)(t+5683636224).
\]

Full derivations and the quotient's monic Weierstrass equation are in
`research/family_A_elliptic.md`.
