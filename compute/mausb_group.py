#!/usr/bin/env python3
"""Exact group law on the two-offset curve through Mausberg's Y-set.

Mausberg's five integers
    z in {330, 870, 2445, 4155, 10482}
lie on
    Y(a,b,c) = {z : z^2+a, z^2+b, z^2+c are squares}
with (a,b,c)=(756000, 15971200, 45130176).

The two-offset curve Y(a,b) is elliptic. Linear combinations of the five
points remain on Y(a,b) but need not lie on Y(a,b,c). This script maps
z |-> (X,Y) on
    Y^2 = X^3 - 2p X^2 + (p^2-4a^2) X,
    p = 4b-2a,
inverts the map by t = Y/(2X), z = (a/t - t)/2, and tests the third
offset. A sixth rational point on the full Y(a,b,c) would give five
positive N sharing four differences after the family-G transpose; a
fifth offset on those six z-values would be a k=5 example.

No sixth integer z is found below the bound, and small Mordell-Weil
combinations that are new on Y(a,b) fail the third square.
"""

from __future__ import annotations

import math
import os
import sys
from fractions import Fraction
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extra_column import extra_offsets
from factor_diff import _is_square, common_differences

A, B, C = 756000, 15971200, 45130176
ZS = [330, 870, 2445, 4155, 10482]
P_COEF = 4 * B - 2 * A
A_WEIER = -2 * P_COEF
B_WEIER = P_COEF * P_COEF - 4 * A * A


def is_on_Y(z: int, a=A, b=B, c=C) -> bool:
    return _is_square(z * z + a) and _is_square(z * z + b) and _is_square(z * z + c)


def is_square_Q(r: Fraction) -> bool:
    if r < 0:
        return False
    n, d = r.numerator, r.denominator
    return math.isqrt(n) ** 2 == n and math.isqrt(d) ** 2 == d


def sqrt_Q(r: Fraction) -> Fraction | None:
    if not is_square_Q(r):
        return None
    return Fraction(math.isqrt(r.numerator), math.isqrt(r.denominator))


def z_to_XY(z) -> tuple[Fraction, Fraction]:
    z = Fraction(z)
    x = sqrt_Q(z * z + A)
    y = sqrt_Q(z * z + B)
    if x is None or y is None:
        raise ValueError(f"{z} not on Y(a,b)")
    t = x - z
    v = 2 * t * y
    X = 2 * (v + t * t) + P_COEF
    Y = 4 * t * (v + t * t) + 2 * P_COEF * t
    return X, Y


def XY_to_z(X: Fraction, Y: Fraction) -> Fraction | None:
    if X == 0:
        return None
    t = Y / (2 * X)
    if t == 0:
        return None
    return (Fraction(A) / t - t) / 2


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 + y2 == 0:
        return None
    if x1 == x2:
        if y1 == 0:
            return None
        lam = (3 * x1 * x1 + 2 * A_WEIER * x1 + B_WEIER) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam - A_WEIER - x1 - x2
    y3 = lam * (x1 - x3) - y1
    return (x3, y3)


def mul(n: int, P):
    if n < 0:
        return mul(-n, (P[0], -P[1]))
    acc = None
    Q = P
    while n:
        if n & 1:
            acc = add(acc, Q)
        Q = add(Q, Q)
        n >>= 1
    return acc


def on_Yabc(z: Fraction) -> bool:
    return is_square_Q(z * z + A) and is_square_Q(z * z + B) and is_square_Q(z * z + C)


def transpose_grid(zs):
    y0 = zs[0]
    xs = [y0]
    for off in (A, B, C):
        xs.append(math.isqrt(y0 * y0 + off))
    ds = [2 * x for x in xs]
    ns = [z * z - y0 * y0 for z in zs[1:]]
    return ns, ds


def main() -> None:
    assert all(is_on_Y(z) for z in ZS)
    pts = [z_to_XY(z) for z in ZS]
    for z, P in zip(ZS, pts):
        assert XY_to_z(*P) == z
        X, Y = P
        assert Y * Y == X ** 3 + A_WEIER * X ** 2 + B_WEIER * X

    extra = [z for z in range(1, 50000) if z not in ZS and is_on_Y(z)]
    print("extra integer z below 5e4", extra)

    news_ab = []
    news_abc = []
    for coeffs in product((-1, 0, 1), repeat=5):
        if all(c == 0 for c in coeffs):
            continue
        R = None
        for c, P in zip(coeffs, pts):
            if c:
                R = add(R, mul(c, P))
        if R is None:
            continue
        z = XY_to_z(*R)
        if z is None:
            continue
        if on_Yabc(z):
            if z not in [Fraction(x) for x in ZS] and z not in [-Fraction(x) for x in ZS]:
                news_abc.append((z, coeffs))
        elif is_square_Q(z * z + A) and is_square_Q(z * z + B):
            if z.denominator != 1 or abs(int(z)) not in ZS:
                news_ab.append((z, coeffs))
    print("new Y(a,b,c) points in {-1,0,1}-span (excluding ±seeds)", news_abc[:10], "count", len(news_abc))
    print("sample new Y(a,b) points failing c", [(z, cf) for z, cf in news_ab[:5]], "count", len(news_ab))

    ns, ds = transpose_grid(ZS)
    print("transposed N", ns)
    print("transposed d", ds)
    print("intersection", sorted(common_differences(ns)))
    print("Y extra offsets", extra_offsets(ZS))


if __name__ == "__main__":
    main()
