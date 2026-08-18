# Method-family registry

Classification is by mathematical idea, not wording. Early rounds do not broadcast a favoured candidate construction across families.

| ID | Family | Status | Last change |
|----|--------|--------|-------------|
| A | Elliptic-curve slices (fixed or slowly varying differences) | blocked for general \(k\); active only for reproducing \(k=3,4\) | round 2 |
| B | Polynomial / rational identities in a **common** parameter | active | round 2 |
| C | Multiplicative composition (Gaussian integers, Kronecker of small blocks) | active | round 2 |
| D | Additive square tables with one side forced to squares | active | round 2 |
| E | Geometric re-embedding (odd distances, rational distance sets) | active, low priority | round 2 |
| F | Local–global / disproof | active, independent | round 2 |
| G | Inductive lift \(k\to k+1\) | active | round 2 |

## Block rules

- A family is **blocked** when it stalls on a theorem-strength missing lemma with no new mechanism.
- Re-open only when a new identity, invariant, or construction is proposed.
- A reduction to a statement of the same strength as Erdős 885 is not progress.

## Family notes

### A

Jiménez-Urroz: positive-rank elliptic curve \(\Rightarrow\) infinitely many \(n\) sharing three fixed differences. Bremner: special locus for four differences. Generic five-difference slices have genus \(>1\). Round 2 reconstructed the Weierstrass model \(Y^2=X(X-49140)(X-37620)\) and checked that adjoining \(2P\) to the three seed points does **not** create a fourth common difference. No new mechanism that would un-block general \(k\). The restatement “some \(\mathbf d\) with \(\ge k\) rational points on \(C_{\mathbf d}\)” is equivalent to 885 after scaling and is not progress.

### B

Seek \(N_i(t),d_j(t),s_{ij}(t)\in\mathbb{Q}(t)\) with \(s_{ij}^2=4N_i+d_j^2\) identically. All functions of one parameter \(t\), not separated variables \(x,y\). The separated identity \(A(x)+D(y)^2=S(x,y)^2\) is degenerate. Explicit identities exist for \(k=2\) (polynomial) and \(k=3\) (rational Euler/Heron translate). A fourth square on a generic common translate has genus \(1+2^{m-2}(m-3)\) and is not identically a square. This remains the most plausible general-\(k\) route, and it is still missing the \(k\ge 4\) identity.

### C

Rank-1 tables \(u_{ij}=x_i y_j\) collapse to a single row. Composition of quadratic forms (Hurwitz–Radon) lives in dimensions \(1,2,4,8\) and does not by itself produce an arbitrary-\(k\) grid with constant row products and constant column differences.

### D

Choudhry gives unrestricted additive square tables for sizes \((4,4)\) and \((5,3)\). The extra condition that a strictly positive translate of \(\{B_j\}\) consists of squares is exactly 885. Automatic row-translates make a row zero or negative. No admissible translate was found for the published tables with reduced denominator \(\le 20000\). Bounded \(5\times 5\) searches with cell roots \(\le 2000\) were empty.

### F

The variety is real-nonempty. Squares modulo \(8\) are \(0,1,4\). No modular obstruction for small \(k\) (solutions exist). Any obstruction must start at some \(k_0\ge 5\). Absence of an obstruction is not a proof of existence.

### G

Adding a column to a **fixed** \(k\)-tuple asks those same \(k\) integers to share one more difference. Generically they do not. A lift must move in a positive-dimensional family. Bremner’s \(k=4\) family is one-dimensional; imposing a fifth difference is expected to be zero-dimensional and may be empty. Round 2: the Guiduli/Mausberg fibres are exhaustive (no extra row or column); Mausberg’s five \(z\)-values do not produce a sixth integer \(z<5\cdot 10^4\); adjoining \(2P\) on the \(k=3\) curve does not add a column.

### E

Odd-distance geometry motivated the 1997 paper and was solved independently by Piepmeyer. Other geometric dictionaries (rational distance, Euler brick, hyperbolas \(xy=N\)) are incomplete reductions unless the target problem is already solved. The only geometric identity that helped is the \(k=3\) Heron translate, already recorded in family B. See `research/family_E_geometry.md`.
