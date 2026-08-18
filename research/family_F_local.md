# Family F: local–global / disproof

## Verdict (round 1)

No modular obstruction was found for \(k\le 6\) modulo \(3,5,7,8,16\).

A first script wrongly required the \(N_i\) to be pairwise distinct in \(\mathbb{Z}/m\mathbb{Z}\). That is illegitimate: distinctness is over \(\mathbb{Z}\). In particular, if some \(d_j\) is odd then every \(N_i\) is even (because \(4N+d^2\equiv 5\pmod 8\) is not a square), so there are only four even residues modulo \(8\). For \(k\ge 5\) pigeonhole forces a repeated residue modulo \(8\). That is **not** a local obstruction.

Corrected check: `compute/local_solubility.py`. For every \(k\le 6\) and every tested modulus there exist residues \(N_i,d_j\) satisfying all \(k^2\) congruences \(4N_i+d_j^2\in\mathrm{Sq}(\mathbb{Z}/m\mathbb{Z})\).

Guiduli’s integer solution reduces into these local solutions, as it must.

## What this does not prove

Local solubility plus expected dimension \(2k>0\) does not give a rational point. A Brauer–Manin obstruction on \(X_k\) for large \(k\) remains conceivable. Family F stays open as a disproof route; it currently has **no** certificate of non-existence.

## Real solubility

Take \(N_i>0\), \(d_j>0\). Then \(4N_i+d_j^2>0\), so real square roots exist. The real locus is nonempty and even Zariski-dense in the real points of the expected-dimensional complete intersection.
