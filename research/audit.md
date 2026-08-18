# Adversarial audit log

Classification rule: attack the argument, not the wording. A reduction
to a statement of the same strength as Erdős 885 is not a proof. A
verified example for one \(k\) is not a proof for every \(k\).

## Round 1

| Claim | Attack | Outcome |
|-------|--------|---------|
| Lemma A: \(d\in D(n)\) iff \(4n+d^2\) is square | Elementary; both directions written | Survives |
| Naive expected dimension \(2-(k-2)^2\) | This is not an algebraic dimension of a variety over \(\mathbb Q\). The variety \(s_{ij}^2=4N_i+d_j^2\) has expected dimension \(2k\). | The count explains failed random search; it is **not** a non-existence proof. Recorded in `docs/equivalences.md`. |
| Separated identity \(A(x)+D(y)^2=S(x,y)^2\) cannot prove 885 | The lemma only kills one ansatz | Survives as a restriction on family B, not a disproof |
| “Jiménez-Urroz / Bremner PDFs reproduced” | Publisher fetches failed | Downgraded to independent reconstruction plus zbMATH theorem statements |
| Local obstruction mod 8 for \(k=5\) | First script required distinct residues; invalid | Withdrawn. Uniform local solubility proved. |
| Mausberg \(Y\)-set solves \(k=5\) | Five \(z\)-values give **four** \(N\) and four differences after transpose | Withdrawn as a \(k=5\) claim |

## Round 2

| Claim | Attack | Outcome |
|-------|--------|---------|
| The \(\mathbb Q(t)\) \(3\times3\) identity | Direct expansion / common-translate lemma | Survives as an identity. It does **not** give \(k=4\) identically: the fourth-square fibre is the genus formula \(g=1+2^{m-2}(m-3)\). |
| Weierstrass model \(Y^2=X(X-49140)(X-37620)\) for \((d)=(6,54,111)\) | Checked that the three seed \(N\) map to points on the model and that \(P=(62244,4481568)\) is non-torsion by reduction mod 43 against Mazur | Survives as a reconstruction of the Jiménez-Urroz *mechanism*, not of his numbered equations |
| “Bremner’s parametric family reconstructed” | Only a verified finite \(4\times4\) example is in the repo | **Fails.** The infinite family of 4-sets is cited from the abstract/review, not recovered as formulae. Status: \(k=4\) is known in the literature and independently witnessed by one explicit 4-set; the Bremner parameterisation remains unread. |
| Adding \(2P\) to the three seed points yields a fourth common difference | Complete extra-column search after the correct scaling \(\lambda=36047\) | **Fails.** The four integers share exactly the three scaled differences \(216282,1946538,4001217\). |
| Linear combinations on Mausberg’s \(Y(a,b)\) automatically satisfy the third offset \(c\) | Exact group law; test \(z^2+c\) | **Fails.** New points lie on the elliptic curve \(Y(a,b)\) and not on \(Y(a,b,c)\). No sixth integer \(z<5\cdot10^4\). |
| Choudhry additive tables become 885 after a translate | Automatic translate using a row makes one \(N=0\) or some \(N<0\) | Survives as a trap. Bounded denominator search \(q\le20000\) found no admissible translate. Not a proof that none exists. |
| Uniform local solubility \(\Rightarrow\) the conjecture is true | Brauer–Manin and integral points can still obstruct | **Fails as a proof.** Family F remains a disproof search, not an existence theorem. |
| Two-column divisor construction solves 885 | It produces arbitrarily many rows and only two columns | Correct lemma, wrong strength. Recovers Erdős–Rosenfeld Proposition 3.2, not the full conjecture. |
| “For every \(k\) some \(\mathbf d\) with \(\ge k\) rational points on \(C_{\mathbf d}\)” | After scaling this is equivalent to 885 | Restatement, not progress. Blocked as a family-A general-\(k\) attack. |

## Standing bans

- Do not announce a favoured incomplete reduction to other families.
- Do not reopen a blocked family without a new identity, invariant, or construction.
- Do not treat a \(k=5\) numerical example, if one appears, as a proof for all \(k\).
- Do not start Lean 4 verification of a theorem that has not survived this log.

## Missing lemma (concrete, not mood)

One of the following, with a proof, would finish the problem:

1. **Identity lift.** Polynomials or rational functions \(N_i(t),d_j(t),s_{ij}(t)\) in one common parameter, for every \(k\), satisfying \(s_{ij}^2=4N_i+d_j^2\) with distinct positive specialisations. Families of this type are known for \(k=2\) and \(k=3\) only.
2. **Inductive step.** A map taking a nondegenerate \(k\times k\) grid to a nondegenerate \((k+1)\times(k+1)\) grid. No such map is known; extra-column searches on the known seeds are empty.
3. **Square side of a \(k\times k\) additive table.** Integers \(A_i>0\), \(B_j=d_j^2\), \(A_i+B_j\) all squares, for every \(k\). Unrestricted additive tables are a strictly weaker problem.
4. **Disproof.** A \(k\ge5\) for which the positive integral grid is empty, with a complete obstruction (not a failed search, not a restated conjecture). Local solubility is not such an obstruction.
