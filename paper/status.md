# Status of Erdős 885 (not a claimed proof)

This note is a research status report. It does not assert that the
Erdős–Rosenfeld conjecture holds for every \(k\), and it does not assert
that the conjecture fails for some \(k\).

## The problem

For \(n\ge 1\) let \(D(n)=\{\lvert a-b\rvert:n=ab\}\). The conjecture asks
whether for every integer \(k\ge 1\) there exist \(N_1<\cdots<N_k\) with
\(\lvert\bigcap_i D(N_i)\rvert\ge k\).

The cases \(k=2,3,4\) are known (Erdős–Rosenfeld 1997, Jiménez-Urroz 1999,
Bremner 2019). Independent witnesses for those three cases are recorded
in `examples/`. The general case is open.

## Two questions a complete proof must answer

### (1) How is the argument different from ErRo, Jiménez-Urroz, Bremner, and the additive-square literature?

- Erdős–Rosenfeld produce arbitrarily many integers sharing **two**
  fixed differences, and prove that a **fixed** pair of differences is
  shared by only finitely many integers.
- Jiménez-Urroz upgrade the second coordinate from 2 to 3 by running a
  positive-rank elliptic curve of three simultaneous squares, then
  scaling. The reconstruction in this repository is the curve
  \(Y^2=X(X-49140)(X-37620)\) for differences \(6,54,111\), with a
  non-torsion point. This is still three columns.
- Bremner produces infinitely many **4-element** sets with four common
  differences, necessarily on a special locus: a generic four-difference
  slice has genus 5. The present repository verifies one explicit
  \(4\times4\) grid; it does not recover Bremner’s parameterisation from
  the unread PDF.
- Choudhry (arXiv:2508.07806) produces unrestricted additive square
  tables \(A_i+B_j=\mathrm{square}\) of sizes \((3,3)\), \((5,3)\),
  \((4,4)\). Erdős 885 additionally requires that the \(B_j\) be squares
  (or a strictly positive translate of squares). That extra condition is
  open. An automatic translate along a row of the table makes a row zero
  or negative and does not solve 885.

A proof for every \(k\) must do something that none of these four texts
do: either force \((k-1)^2\) square conditions to be algebraically
dependent for arbitrary \(k\), give a lift \(k\to k+1\), or give a
genuine local-to-global existence theorem on the variety
\(s_{ij}^2=4N_i+d_j^2\).

No such argument is supplied here.

### (2) What new mathematical insight crosses the obstruction \(2-(k-2)^2\)?

The naive integer count — \(2k-1\) free first-row/column entries minus
\((k-1)^2\) independent “is a square” conditions — is negative for
\(k\ge 4\). That count is why unstructured search fails. It is **not**
the dimension of the algebraic variety, which is expected to be \(2k\)
before positivity. The genuine geometric obstruction for the
*fixed-difference* method is the genus formula
\(g=1+2^{m-2}(m-3)\) for \(m\) simultaneous squares \(x+d_j^2\).

Known crossings of the obstruction, all of limited range:

- \(k=2\): a polynomial identity in one parameter (genus 0).
- \(k=3\): a rational identity coming from a second common square
  translate of three linear polynomials (elliptic in \(t\) if a fourth
  square is imposed, not identically square).
- \(k=4\): a special locus, witnessed by an explicit grid, not by an
  identity in this repository.

The missing insight is a mechanism that makes the \((k-1)^2\) square
conditions dependent **for every** \(k\). Candidate sources (Gaussian
composition, Kronecker of small blocks, Pell units, unrestricted
additive tables) have been audited and fail to do this, or reduce to a
problem of the same strength. Local solubility holds for every \(k\) and
therefore does not supply a disproof.

Until that insight exists, there is nothing to formalise in Lean 4.

## What this repository does claim

Only the lemmas under `lemmas/`, the verified examples under
`examples/`, and the family verdicts under `research/`. The object still
required for a complete solution is written in
`lemmas/missing_for_all_k.md`.
