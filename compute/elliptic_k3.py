#!/usr/bin/env python3
"""Exact arithmetic on the reconstructed Jiménez-Urroz curve.

Curve (family A):
    Y^2 = X(X-49140)(X-37620)
arising from the three differences (6, 54, 111).

This script
- generates multiples of the non-torsion point corresponding to N=112,
- scales finitely many rational N's to integers sharing those three
  differences,
- runs a complete extra-column search on those integers.

A fourth common difference would be a k=4 example on this slice; a fifth
would be a k=5 example. Neither appears for the small combinations tested
here. That is expected: a generic extra difference raises the genus.
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction
from math import gcd, isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extra_column import differences_from_anchor

AA = -86760
BB = 1848646800
AOFF = 2880  # 54^2 - 6^2
D1, D2, D3 = 6, 54, 111
P = (Fraction(62244), Fraction(4481568))
Q = (Fraction(54340), Fraction(2173600))
R = (Fraction(51300), Fraction(1231200))


def add(P1, P2):
    if P1 is None:
        return P2
    if P2 is None:
        return P1
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2 and y1 + y2 == 0:
        return None
    if x1 == x2:
        if y1 == 0:
            return None
        lam = (3 * x1 * x1 + 2 * AA * x1 + BB) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam - AA - x1 - x2
    y3 = lam * (x1 - x3) - y1
    return (x3, y3)


def mul(n: int, Pt):
    if n < 0:
        x, y = Pt
        return mul(-n, (x, -y))
    acc = None
    Qpt = Pt
    while n:
        if n & 1:
            acc = add(acc, Qpt)
        Qpt = add(Qpt, Qpt)
        n >>= 1
    return acc


def xy_to_Nz(X: Fraction, Y: Fraction):
    t = 2 * AOFF * X / Y
    z = (t * t - AOFF) / (2 * t)
    N = (z * z - D1 * D1) / 4
    return N, z


def is_square_Q(r: Fraction) -> bool:
    if r < 0:
        return False
    n, d = r.numerator, r.denominator
    return isqrt(n) ** 2 == n and isqrt(d) ** 2 == d


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def scale_and_search(points: dict[str, tuple[Fraction, Fraction]], names: list[str]) -> None:
    data = []
    for name in names:
        N, z = xy_to_Nz(*points[name])
        ok = all(is_square_Q(4 * N + d * d) for d in (D1, D2, D3))
        print(f"  {name}: N={N} z={z} three-diffs={ok}", flush=True)
        data.append((name, N, z))
    lam = 1
    for _, _, z in data:
        lam = lcm(lam, z.denominator)
    zs = [int(abs(lam * z)) for _, _, z in data]
    Ns = [int(lam * lam * N) for _, N, _ in data]
    ds = differences_from_anchor(zs, lam * D1)
    print(f"  lambda={lam}")
    print(f"  integer N={Ns}")
    print(f"  complete positive common differences from extra-column search: {ds}")
    expected = sorted(lam * d for d in (D1, D2, D3))
    print(f"  expected scaled {{6,54,111}}={expected}")
    print(f"  extra columns: {sorted(set(ds) - set(expected))}")


def main() -> None:
    assert P[1] ** 2 == P[0] * (P[0] - 49140) * (P[0] - 37620)
    points = {
        "P": P,
        "Q": Q,
        "R": R,
        "2P": mul(2, P),
        "P+Q": add(P, Q),
    }
    print("2P is non-integral (Jiménez-Urroz scaling is essential)")
    N2, z2 = xy_to_Nz(*points["2P"])
    print(f"  2P: N={N2} z={z2}")
    for names in (
        ["P", "Q", "R"],
        ["P", "Q", "R", "2P"],
        ["P", "Q", "R", "P+Q"],
    ):
        print("===", names)
        scale_and_search(points, names)


if __name__ == "__main__":
    main()
