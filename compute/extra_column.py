#!/usr/bin/env python3
"""Exhaustive extra-column search for a finite list of row square-roots.

Given integers z_1,...,z_m, find every offset α such that z_i^2+α is a
square for all i. This enumerates every common extra difference of the
corresponding N_i once an anchor difference d_1 is fixed, because
d^2 = d_1^2 + α.

The search is complete: it factors z_1^2-z_2^2 and tests the remaining
rows. It is not a proof for general k.
"""

from __future__ import annotations

import math
from collections.abc import Iterable


def _is_square(m: int) -> bool:
    if m < 0:
        return False
    r = math.isqrt(m)
    return r * r == m


def _divisors_signed(n: int) -> list[int]:
    n = abs(int(n))
    out = []
    r = math.isqrt(n)
    for i in range(1, r + 1):
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
    signed = []
    for d in out:
        signed.append(d)
        signed.append(-d)
    return signed


def extra_offsets(zs: Iterable[int]) -> list[int]:
    zs = [int(z) for z in zs]
    if len(zs) < 2:
        raise ValueError("need at least two rows")
    z0, z1 = zs[0], zs[1]
    delta = z0 * z0 - z1 * z1
    if delta == 0:
        return []
    alphas: set[int] = set()
    for f in _divisors_signed(delta):
        if f == 0 or delta % f:
            continue
        g = delta // f
        if (f + g) % 2:
            continue
        x = (f + g) // 2
        alpha = x * x - z0 * z0
        if all(_is_square(z * z + alpha) for z in zs):
            alphas.add(alpha)
    return sorted(alphas)


def differences_from_anchor(zs: Iterable[int], d1: int) -> list[int]:
    """Positive d such that 4N_i + d^2 is square whenever z_i^2 = 4N_i + d1^2."""
    d1 = int(d1)
    out = []
    for alpha in extra_offsets(zs):
        dd = d1 * d1 + alpha
        if dd > 0 and _is_square(dd):
            out.append(math.isqrt(dd))
    return sorted(set(out))


if __name__ == "__main__":
    # The Jiménez-Urroz seed: three n sharing 6,54,111 and nothing else.
    zs = [22, 62, 114]
    print("PQR diffs", differences_from_anchor(zs, 6))
    # Mausberg Y-set z-values (four columns after transpose).
    zs_m = [330, 870, 2445, 4155, 10482]
    print("Mausberg Y offsets", extra_offsets(zs_m))
