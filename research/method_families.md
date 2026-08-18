# Method-family registry

Classification is by mathematical idea, not wording. Early rounds do not broadcast a favoured candidate construction across families.

| ID | Family | Status | Last change |
|----|--------|--------|-------------|
| A | Elliptic-curve slices (fixed or slowly varying differences) | blocked for general \(k\); active only for reproducing \(k=3,4\) | round 1 |
| B | Polynomial / rational identities in a **common** parameter | active | round 1 |
| C | Multiplicative composition (Gaussian integers, Kronecker of small blocks) | active | round 1 |
| D | Additive square tables with one side forced to squares | active | round 1 |
| E | Geometric re-embedding (odd distances, rational distance sets) | active, low priority | round 1 |
| F | Local–global / disproof | active, independent | round 1 |
| G | Inductive lift \(k\to k+1\) | active | round 1 |

## Block rules

- A family is **blocked** when it stalls on a theorem-strength missing lemma with no new mechanism.
- Re-open only when a new identity, invariant, or construction is proposed.
- A reduction to a statement of the same strength as Erdős 885 is not progress.

## Family notes

### A

Jiménez-Urroz: positive-rank elliptic curve \(\Rightarrow\) infinitely many \(n\) sharing three fixed differences. Bremner: special locus for four differences. Generic five-difference slices have genus \(>1\). No new mechanism in round 1 that would un-block general \(k\).

### B

Seek \(N_i(t),d_j(t),s_{ij}(t)\in\mathbb{Q}(t)\) with \(s_{ij}^2=4N_i+d_j^2\) identically. All functions of one parameter \(t\), not separated variables \(x,y\). The separated identity \(A(x)+D(y)^2=S(x,y)^2\) is degenerate (lemma in `lemmas/`).

### C

Rank-1 tables \(u_{ij}=x_i y_j\) collapse to a single row. Composition of quadratic forms (Hurwitz–Radon) lives in dimensions \(1,2,4,8\) and does not by itself produce an arbitrary-\(k\) grid with constant row products and constant column differences.

### D

Choudhry gives unrestricted additive square tables for sizes \((4,4)\) and \((5,3)\). The extra condition that \(\{B_j-B_1\}\) are squares is exactly 885 and is open in that language.

### F

The variety is real-nonempty. Squares modulo \(8\) are \(0,1,4\). No modular obstruction for small \(k\) (solutions exist). Any obstruction must start at some \(k_0\ge 5\). Absence of an obstruction is not a proof of existence.

### G

Adding a column to a **fixed** \(k\)-tuple asks those same \(k\) integers to share one more difference. Generically they do not. A lift must move in a positive-dimensional family. Bremner’s \(k=4\) family is one-dimensional; imposing a fifth difference is expected to be zero-dimensional and may be empty.
