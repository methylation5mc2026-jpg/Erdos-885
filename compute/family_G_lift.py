#!/usr/bin/env python3
"""Exact seed fibers and a bounded rational 4-to-5 lift search.

The seed-row searches are exhaustive: two fixed differences reduce the
possible positive integers N to divisor pairs of e^2-d^2.  The rational
search is exhaustive only through the requested denominator bound.
"""

from __future__ import annotations

import argparse
import math
from collections.abc import Iterable

from factor_diff import (
    GUIDULI_1_DIFFS,
    GUIDULI_1_NS,
    GUIDULI_2_DIFFS,
    GUIDULI_2_NS,
    MAUSBERG_DIFFS,
    MAUSBERG_NS,
    _is_square,
    common_differences,
    verify_matrix,
)


SEEDS = (
    ("Guiduli 1", GUIDULI_1_DIFFS, GUIDULI_1_NS),
    ("Guiduli 2", GUIDULI_2_DIFFS, GUIDULI_2_NS),
    ("Mausberg", MAUSBERG_DIFFS, MAUSBERG_NS),
)

# Five points with three common positive square translates.  The script
# verifies all fifteen identities before using the packet.
ANCHOR_POINTS = [330, 870, 2445, 4155, 10482]
ANCHOR_SHIFTS = [756000, 15971200, 45130176]


def exact_integer_fiber(ds: Iterable[int]) -> tuple[list[int], list[int]]:
    """Return all pair candidates and all positive N sharing every d in ds."""
    differences = sorted(set(ds))
    if len(differences) < 2 or differences[0] < 0:
        raise ValueError("need at least two distinct nonnegative differences")

    d, e = differences[:2]
    delta = e * e - d * d
    candidates: set[int] = set()
    solutions: set[int] = set()

    # If x^2=4N+d^2 and y^2=4N+e^2, then
    # (y-x)(y+x)=e^2-d^2.  Conversely every valid factor pair is tested.
    for u in range(1, math.isqrt(delta) + 1):
        if delta % u:
            continue
        v = delta // u
        if (u + v) % 2:
            continue
        x = (v - u) // 2
        numerator = x * x - d * d
        if numerator <= 0 or numerator % 4:
            continue
        n = numerator // 4
        candidates.add(n)
        if all(_is_square(4 * n + difference * difference) for difference in differences):
            solutions.add(n)

    return sorted(candidates), sorted(solutions)


def exact_seed_report() -> None:
    for name, ds, known in SEEDS:
        candidates, solutions = exact_integer_fiber(ds)
        intersection = sorted(common_differences(known))
        print(f"{name}:")
        print(f"  pair-fiber candidates: {len(candidates)}")
        print(f"  all N sharing listed differences: {solutions}")
        print(f"  equals supplied N: {solutions == sorted(known)}")
        print(f"  exact common differences of supplied N: {intersection}")
        print(f"  no extra common difference: {intersection == sorted(ds)}")


def anchor_square_roots() -> list[list[int]]:
    roots: list[list[int]] = []
    for y in ANCHOR_POINTS:
        row = []
        for shift in ANCHOR_SHIFTS:
            value = y * y + shift
            root = math.isqrt(value)
            if root * root != value:
                raise AssertionError(f"anchor packet failed at y={y}, shift={shift}")
            row.append(root)
        roots.append(row)
    return roots


def transposed_k4() -> tuple[list[int], list[int]]:
    """Transpose the verified 5-point/3-shift packet into a positive k=4 grid."""
    roots = anchor_square_roots()
    y0 = ANCHOR_POINTS[0]
    ns = [y * y - y0 * y0 for y in ANCHOR_POINTS[1:]]
    # Include shift zero.  Doubling clears all parity issues:
    # (2*root)^2 = 4*(y^2-y0^2) + (2*root_at_y0)^2.
    ds = [2 * y0] + [2 * root for root in roots[0]]
    if not verify_matrix(ns, ds):
        raise AssertionError("transposed k=4 grid failed")
    return ns, ds


def factor_integer(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        old = divisors
        divisors = []
        power = 1
        for _ in range(exponent + 1):
            divisors.extend(d * power for d in old)
            power *= prime
    return divisors


def rational_row_lift(max_denominator: int) -> tuple[int, list[tuple[int, int]]]:
    """Search the one-dimensional row family, then impose its last square.

    Let d0<d1<d2<d3 be the transposed k=4 differences and z=p/q.  The
    first-three-column family is

        x1^2 = z^2 + (d1^2-d0^2),
        x2^2 = z^2 + (d2^2-d0^2).

    The extra condition is x3^2=z^2+(d3^2-d0^2).  For each reduced
    denominator q <= max_denominator, factor pairs of
    (d1^2-d0^2)*q^2 enumerate every possible numerator p.
    """
    _, ds = transposed_k4()
    d0 = ds[0]
    offsets = [d * d - d0 * d0 for d in ds[1:]]
    base_factors = factor_integer(offsets[0])
    survivors: set[tuple[int, int]] = set()
    candidates = 0

    for q in range(1, max_denominator + 1):
        factors = base_factors.copy()
        for prime, exponent in factor_integer(q).items():
            factors[prime] = factors.get(prime, 0) + 2 * exponent
        product = offsets[0] * q * q

        for a in divisors_from_factorization(factors):
            if a * a > product:
                continue
            b = product // a
            if (a + b) % 2:
                continue
            p = (b - a) // 2
            if p <= d0 * q or math.gcd(p, q) != 1:
                continue
            candidates += 1
            if all(_is_square(p * p + offset * q * q) for offset in offsets[1:]):
                survivors.add((p, q))

    return candidates, sorted(survivors)


def lift_report(max_denominator: int) -> None:
    ns, ds = transposed_k4()
    roots = [
        [math.isqrt(4 * n + d * d) for d in ds]
        for n in ns
    ]
    candidates, all_rows = exact_integer_fiber(ds)
    common_ds = sorted(common_differences(ns))
    rational_candidates, rational_survivors = rational_row_lift(max_denominator)

    print("Transposed k=4 pattern:")
    print(f"  N: {ns}")
    print(f"  d: {ds}")
    print(f"  s rows: {roots}")
    print(f"  verified: {verify_matrix(ns, ds)}")
    print(f"  exact pair-fiber candidates for another integer N: {len(candidates)}")
    print(f"  all positive integer N sharing all four d: {all_rows}")
    print(f"  exact common differences: {common_ds}")
    print("One-dimensional row lift:")
    print(f"  offsets from d0: {[d*d-ds[0]*ds[0] for d in ds[1:]]}")
    print(f"  reduced denominators searched: 1 <= q <= {max_denominator}")
    print(f"  first-square factor-pair candidates: {rational_candidates}")
    print(f"  points surviving the extra square: {rational_survivors}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max-denominator",
        type=int,
        default=20_000,
        help="exhaustive reduced-denominator bound for the rational lift",
    )
    args = parser.parse_args()
    if args.max_denominator < 1:
        parser.error("--max-denominator must be positive")
    exact_seed_report()
    lift_report(args.max_denominator)


if __name__ == "__main__":
    main()
