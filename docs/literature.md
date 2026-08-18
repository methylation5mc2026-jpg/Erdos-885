# Literature review: Erdős 885

## Primary sources

### Erdős–Rosenfeld 1997

Paul Erdős and Moshe Rosenfeld, *The factor-difference set of integers*, Acta Arithmetica **79** (1997), 353–359.

The paper defines \(D(n)\) and poses Conjecture 1, which is Erdős 885. Motivation is the odd-integral-distance problem in the plane: Turán’s theorem limits the odd-distance graph to a balanced complete tripartite graph, and a failed axis-aligned construction reduces to many integers sharing a large common subset of \(D(\,\cdot\,)\). Piepmeyer later solved the geometric problem by another construction; the arithmetic question remained.

Proved facts:

- **Proposition 3.1.** For any distinct integers \(a,b\) there are only finitely many \(M\) with \(\{a,b\}\subset D(M)\). Proof: if \(a=2\alpha\), \(b=2\beta\) then \(x^2-\alpha^2=y^2-\beta^2\) yields a factorization of the fixed integer \((\alpha-\beta)(\alpha+\beta)\). The mixed-parity case reduces by doubling.
- **Proposition 3.2.** For every \(k\) there exist \(N_1<\cdots<N_k\) with \(\lvert\bigcap D(N_i)\rvert\ge 2\). Construction: split a product of distinct odd primes into two blocks to produce \(\alpha,\beta\), then use all factorizations of \(\prod p_i\) to manufacture many \(M\) sharing the two differences \(2\alpha,2\beta\).

They could not produce a pair sharing arbitrarily many differences. Guiduli supplied two triples of integers each sharing **four** differences:

- \(\{420,3780,14940,76860\}\subset D(6925500)\cap D(37901500)\cap D(108448956)\)
- \(\{420,3780,61695,154332\}\subset D(2778300)\cap D(862552800)\cap D(5400442044)\)

Section 4 studies gaps in a single \(D(n)\) (\(d_1(n)\ge 2 n^{1/4}\), eight consecutive integers, Hua/Tarry/PTE). That is a neighbouring problem, not 885.

### Jiménez-Urroz 1999

Jorge Jiménez-Urroz, *A note on a conjecture of Erdős and Rosenfeld*, Journal of Number Theory **78** (1999), 140–143.

The paper cites Silverman’s *Arithmetic of Elliptic Curves*. The MaRDI/zbMATH review states the theorem: for every \(k\) there is a \(k\)-element set of positive integers whose factor-difference sets have intersection of cardinality at least \(3\). This is the elliptic-curve upgrade of Proposition 3.2, and it implies the original conjecture for \(k=3\).

Mechanism (standard translation): three fixed differences produce the curve of \(X\) such that \(X+d_1^2,X+d_2^2,X+d_3^2\) are all squares, birationally an elliptic curve. Positive Mordell–Weil rank yields infinitely many \(n\) sharing those three differences; any \(k\) of them give the reviewed theorem, and any three of them give Erdős 885 for \(k=3\).

The original PDF was not recovered in this workspace (publisher fetches failed). An independent Weierstrass model for the differences \((6,54,111)\) is recorded in `research/family_A_elliptic.md`; it reconstructs the mechanism (positive rank \(\Rightarrow\) arbitrarily many \(n\) sharing three differences after scaling) rather than Jiménez-Urroz’s numbered equations.

### Bremner 2019

Andrew Bremner, *On a problem of Erdős related to common factor differences*, International Journal of Number Theory **15** (2019), 1059–1068.

Abstract: the result is true for \(k=4\), by producing infinitely many 4-element sets of integers with four common factor differences. MSC 11B75, 11G05, 11D41. The phrase “the ideas of this paper can be extended” does **not** supply a proof for \(k=5\): the expected dimension of a generic slice with five fixed differences is a higher-genus curve.

The original PDF was not recovered here. The obstruction to a naive extension is recorded in `research/method_families.md`.

### Formal statements and partial computational notes

- DeepMind Formal Conjectures: `FormalConjectures/ErdosProblems/885.lean` states the problem; the \(k=2,3,4\) variants are marked solved but still `sorry`.
- Forum note of Sam Mausberg (Lean/Aristotle): \(|Y(756000,15971200,45130176)|\ge 5\), so there is no universal bound \(|Y(a,b,c)|\le 4\); and the exact computation \(D(79200)\cap D(227205)\cap D(1258560)=\{36,468,692,1028\}\). The \(Y\)-set of five integers transposes to a \((|N_s|,|\cap|)=(4,4)\) grid, not a \(k=5\) example. The triple \((79200,227205,1258560)\) is a \((3,4)\) configuration of Guiduli type. Neither solves \(k=5\).

## Neighbouring literature (transfer, not reduction)

- Lothar Piepmeyer, *The maximum number of odd integral distances between points in the plane*, Discrete Comput. Geom. **16** (1996), 113–115. Solves the geometric motivation of ErRo, not 885.
- L.-K. Hua, *On Tarry’s problem*, Quart. J. Math. Oxford **9** (1938), 313–320. Cited by ErRo for equal-moment partitions (small differences of a **single** \(n\)).
- Ajai Choudhry, *Two sets of integers such that all elements of the sumset of the two sets are perfect squares*, arXiv:2508.07806 (2025). Constructs additive square tables of sizes \((3,3)\), \((5,3)\), \((4,4)\). Erdős 885 is the special case in which one set is a translate of squares.
- Diophantine \(D(n)\)-m-tuples (Dujella et al.): \(a_ia_j+n\) is square. Different bilinear shape from \(4N+d^2\); techniques (induced elliptic curves, rank records) transfer, theorems do not.
- Math StackExchange 3099983: a \(5\times 5\) additive square table with the last entry missing is a long-standing computational obstruction, warning against unstructured search for \(k=5\).

## Why the problem is hard

1. For fixed differences, Faltings kills generic \(k\ge 4\) slices.
2. Unstructured integer search faces \(2-(k-2)^2\) naive codimension.
3. There is no non-degenerate rational identity \(A(x)+D(y)^2=S(x,y)^2\) in two separated variables (see `lemmas/no_separated_rational_identity.md`). A proof for all \(k\) must use a **simultaneous** parameter, a degenerate locus, or a local-to-global existence theorem, not a product-type closed form.

## What would be new

A solution must either (i) exhibit, for every \(k\), an explicit point on the variety \(s_{ij}^2=4N_i+d_j^2\) with distinct positive \(N_i,d_j\), or (ii) prove no such point exists for some \(k\). Existing work stops at \(k=4\) by elliptic-curve special loci. The missing insight is a mechanism that forces the \((k-1)^2\) square conditions to be algebraically dependent for every \(k\), or a genuine local-global argument on the \(2k\)-dimensional variety.
