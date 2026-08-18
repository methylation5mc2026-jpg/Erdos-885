# The missing lemma for all \(k\)

Erdős 885 is not proved in this repository. The four statements below
are the concrete remaining targets. Any one of them, with a complete
proof, would finish the problem. Restating 885 in other language is not
one of the four.

## 1. Common-parameter identity for every \(k\)

Find, for each \(k\ge 1\), rational functions
\(N_i(t),d_j(t),s_{ij}(t)\in\mathbb Q(t)\) such that

\[
s_{ij}(t)^2=4N_i(t)+d_j(t)^2
\]

holds identically, and such that some specialisation \(t=t_0\in\mathbb Q\)
gives \(k\) distinct positive integers \(N_i\) and \(k\) distinct positive
differences \(d_j\).

Known: \(k=2\) (polynomial) and \(k=3\) (rational, Euler/Heron translate).
Obstruction already proved for a *separated* two-variable ansatz, and for
imposing a fourth square identically on a generic common translate.

## 2. Inductive lift

A proven construction that takes a nondegenerate integer solution of size
\(k\) to one of size \(k+1\). Extra-column and extra-row searches on the
known Guiduli, Mausberg, Jiménez-Urroz, and Bremner-indexed seeds are
empty; those searches are not a proof that no lift exists on a
positive-dimensional family.

## 3. Square side of an additive table

For every \(k\), integers \(A_i>0\) and \(d_j>0\) such that every
\(A_i+d_j^2\) is a square. Equivalently: a \(k\times k\) additive square
table whose column vector is a translate of squares, with all rows
strictly positive after the translate. Unrestricted additive tables
(Choudhry) are strictly weaker.

## 4. Disproof for some \(k\ge 5\)

A complete obstruction showing that no positive integer \(k\times k\)
grid exists. Uniform solubility over \(\mathbb R\) and every \(\mathbb Q_p\)
rules out a local reason. A failed numerical search is not a disproof.

## Explicitly not missing lemmas

- “There exists \(\mathbf d\) such that \(C_{\mathbf d}\) has at least
  \(k\) rational points.” After scaling this is equivalent to 885.
- “Some elliptic curve of high rank attached to five fixed differences
  has a rational point.” That is the \(k=5\) case of family A, already
  blocked as a general-\(k\) method, and is not proved here even for
  \(k=5\).
- A \(5\times5\) additive square table with one entry missing.
