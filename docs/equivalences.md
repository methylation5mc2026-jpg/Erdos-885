# Equivalent formulations of Erdős 885

## Original statement

Let \(D(n)=\{\lvert a-b\rvert:n=ab\}\). For every integer \(k\ge 1\), do there exist integers \(N_1<\cdots<N_k\) with \(\lvert\bigcap_i D(N_i)\rvert\ge k\)?

Zero is allowed by the definition: \(0\in D(n)\) if and only if \(n\) is a square. A solution that relies on \(0\) as one of the \(k\) common differences is formally valid but degenerate, and is not treated as a complete solution of the intended arithmetic problem. All constructions below aim at \(k\) positive common differences.

## Lemma A (square criterion)

**Lemma A.** For integers \(n\ge 1\) and \(d\ge 0\),

\[
d\in D(n)\quad\Longleftrightarrow\quad 4n+d^2\text{ is a perfect square.}
\]

**Proof.** If \(n=ab\) and \(d=\lvert a-b\rvert\), then \((a+b)^2=4ab+(a-b)^2=4n+d^2\). Conversely, if \(4n+d^2=s^2\) with \(s\ge 0\), then \(s\equiv d\pmod{2}\) because \(s^2-d^2=4n\). Set \(a=(s+d)/2\) and \(b=(s-d)/2\). These are integers, \(ab=n\), and \(\lvert a-b\rvert=d\). \(\square\)

## Matrix form

A \(k\)-tuple \(N_1,\dots,N_k\) shares positive differences \(d_1,\dots,d_k\) if and only if there is an integer matrix \((s_{ij})_{1\le i,j\le k}\) with

\[
s_{ij}^2=4N_i+d_j^2.
\]

The rectangle identity

\[
s_{ij}^2+s_{i'j'}^2=s_{ij'}^2+s_{i'j}^2
\]

holds automatically. Equivalently, the matrix of squares is of the form \(A_i+B_j\) with \(A_i=4N_i\) and \(B_j=d_j^2\).

## First-row reconstruction

Given the first row and first column, the remaining squares are determined:

\[
s_{ij}^2=s_{i1}^2+s_{1j}^2-s_{11}^2.
\]

The remaining problem is that each right-hand side must be a square.

## Factor-pair form

Write \(u_{ij}=(s_{ij}-d_j)/2\) and \(v_{ij}=(s_{ij}+d_j)/2\). Then \(u_{ij}v_{ij}=N_i\) (constant on rows) and \(v_{ij}-u_{ij}=d_j\) (constant on columns). So a solution is a \(k\times k\) table of factorizations with constant products on rows and constant differences on columns.

## Homogeneity

If \(\{d_j\}\subset\bigcap_i D(N_i)\) and \(\lambda\ge 1\), then \(\{\lambda d_j\}\subset\bigcap_i D(\lambda^2 N_i)\). Rational points therefore yield integer points after clearing denominators. It is enough to work over \(\mathbb{Q}\).

## Anchored form

Fix an anchor difference \(d_1\) and set \(z=s_{i1}\), \(a_j=d_j^2-d_1^2\). Then \(z^2+a_j\) is a square for each \(j\ge 2\), and \(4N_i=z^2-d_1^2\). For three offsets this is Mausberg's set

\[
Y(a,b,c)=\{z>0:z^2+a,\;z^2+b,\;z^2+c\text{ are squares}\}.
\]

A large \(Y(a,b,c)\) produces many \(N\) sharing **four** differences, not five.

## Additive-square-table form (strictly weaker)

The problem of finding \(A_1,\dots,A_k\) and \(B_1,\dots,B_k\) with every \(A_i+B_j\) a square is strictly weaker: Erdős 885 additionally requires that the \(B_j\) themselves be squares (or a translate of squares). Reducing 885 to the unrestricted additive-square problem is not a solution unless that extra square condition is proved.

## Dimension counts (two different counts)

### Algebraic variety over \(\mathbb{Q}\)

Variables: \(N_i\), \(d_j\), \(s_{ij}\) (\(k^2+2k\) many). Equations: \(s_{ij}^2=4N_i+d_j^2\) (\(k^2\) many). Expected dimension \(2k\), or \(2k-1\) after scaling \((N,d,s)\mapsto(\lambda^2 N,\lambda d,\lambda s)\). The variety is not expected to be empty as a complex variety.

### Naive integer square-conditions

Treating the \(2k-1\) first-row/column integers as free and imposing \((k-1)^2\) “is a square” conditions on integers gives expected dimension \(2-(k-2)^2\), which is negative for \(k\ge 4\). This explains why random integer searches fail for \(k\ge 5\), but it is **not** an algebraic non-existence proof.

### Fixed differences

If \(d_1,\dots,d_k\) are fixed, the condition that \(X+d_j^2\) is a square for all \(j\) is a curve of expected dimension \(1\). For \(k=2\) it is genus \(0\) in the rational sense but has only finitely many **integer** points (Erdős–Rosenfeld). For \(k=3\) it is typically elliptic. For \(k\ge 4\) and generic \(d_j\) the genus is \(>1\), so Faltings gives finitely many rational \(X\). A proof for all \(k\) cannot proceed by freezing the differences and letting only \(N\) vary, except on special degenerate loci of genus \(0\).
