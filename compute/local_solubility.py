#!/usr/bin/env python3
"""Local solubility of s_ij^2 ≡ 4 N_i + d_j^2 (mod m).

Distinctness of N_i is over Z, not over Z/mZ. Requiring distinct residues
is invalid (and wrongly suggested an obstruction for k=5 mod 8).
"""

from __future__ import annotations

import itertools
import random


def squares_mod(m: int) -> set[int]:
    return {i * i % m for i in range(m)}


def admissible_N_for_d(d: int, m: int, sq: set[int]) -> set[int]:
    d2 = (d * d) % m
    return {n for n in range(m) if (4 * n + d2) % m in sq}


def exists_mod(k: int, m: int) -> bool:
    sq = squares_mod(m)
    slots = [admissible_N_for_d(d, m, sq) for d in range(m)]
    # Need k (not necessarily distinct) columns d_j whose admissible-N
    # sets have a common intersection of size at least 1; we then need k
    # residues N_i in that intersection. Repeating a residue is allowed
    # locally. Existence over Z/mZ is: there exist d1..dk and N1..Nk
    # satisfying the k^2 congruences.
    # Equivalent: choose a nonempty family of d's whose common admissible
    # set S is nonempty, then pick N_i in S and d_j in the family.
    for cols in itertools.product(range(m), repeat=k):
        S = set(range(m))
        for d in cols:
            S &= slots[d]
            if not S:
                break
        if S:
            return True
    return False


def exists_mod_fast(k: int, m: int, trials: int = 50000) -> bool:
    """Random search without distinctness; used only as a heuristic."""
    sq = squares_mod(m)
    rng = random.Random(k * 1000 + m)
    slots = [admissible_N_for_d(d, m, sq) for d in range(m)]
    nonempty_d = [d for d in range(m) if slots[d]]
    if not nonempty_d:
        return False
    for _ in range(trials):
        ds = [rng.choice(nonempty_d) for _ in range(k)]
        S = set(range(m))
        ok = True
        for d in ds:
            S &= slots[d]
            if not S:
                ok = False
                break
        if ok and S:
            return True
    return False


def analyze_mod8() -> None:
    sq = squares_mod(8)
    print("mod 8 squares", sorted(sq))
    for d in range(8):
        print(f" d={d} d^2={d*d%8} admissible N={sorted(admissible_N_for_d(d,8,sq))}")
    print(
        "If any d is odd, all N must be even. Even residues mod 8: 0,2,4,6 "
        "(four of them). k=5 integer solutions may repeat residues mod 8."
    )
    print("exists_mod k=5 mod 8", exists_mod(5, 8))
    print("exists_mod k=6 mod 8", exists_mod(6, 8))


def main() -> None:
    analyze_mod8()
    for k in range(1, 7):
        row = []
        for m in (8, 16, 5, 7, 3):
            if m ** k <= 2_000_000:
                row.append(f"{m}:{exists_mod(k, m)}")
            else:
                row.append(f"{m}:fast={exists_mod_fast(k, m)}")
        print(f"k={k}", " ".join(row))


if __name__ == "__main__":
    main()
