#!/usr/bin/env python3
"""Constructive local checks for s_ij^2 = 4*N_i + d_j^2.

Distinct integers need not have distinct residues.  Requiring distinct
residue classes gives false "obstructions" as soon as k is larger than the
modulus.  These witnesses keep N_i and d_j distinct as rational integers
while allowing their residues to coincide.
"""

from __future__ import annotations

def squares_mod(m: int) -> set[int]:
    return {i * i % m for i in range(m)}


def two_adic_data(k: int) -> tuple[list[int], list[int]]:
    """N_i=2i and d_j=2j-1 make every right side 1 modulo 8."""
    return [2 * i for i in range(1, k + 1)], [2 * j - 1 for j in range(1, k + 1)]


def odd_adic_data(k: int, p: int) -> tuple[list[int], list[int]]:
    """For odd p, every right side is in 1+p*Z_p."""
    if p < 3 or p % 2 == 0:
        raise ValueError("p must be odd")
    return [p * i for i in range(1, k + 1)], [1 + p * j for j in range(1, k + 1)]


def verify_residue_witness(ns: list[int], ds: list[int], m: int) -> bool:
    sq = squares_mod(m)
    return (
        len(ns) == len(set(ns))
        and len(ds) == len(set(ds))
        and all((4 * n + d * d) % m in sq for n in ns for d in ds)
    )


def main() -> None:
    for m in (8, 16, 5, 7):
        print(f"mod {m} squares {sorted(squares_mod(m))}")

    for k in (5, 6):
        ns2, ds2 = two_adic_data(k)
        for m in (8, 16):
            print(
                f"k={k} mod {m}: {verify_residue_witness(ns2, ds2, m)} "
                f"(N_i=2i, d_j=2j-1)"
            )

        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            nsp, dsp = odd_adic_data(k, p)
            print(
                f"k={k} mod {p}: {verify_residue_witness(nsp, dsp, p)} "
                f"(N_i={p}i, d_j=1+{p}j)"
            )

    print("Odd-p lift: each right side lies in 1+pZ_p; Hensel at x=1 applies.")
    print("2-adic lift: each right side is 1 mod 8, hence is a square in Z_2.")


if __name__ == "__main__":
    main()
