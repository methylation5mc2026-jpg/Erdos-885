#!/usr/bin/env python3
"""Look for Q(t) identities for small k by undetermined coefficients."""

from __future__ import annotations

import itertools
import math


def is_poly_square(coeffs: list[int]) -> list[int] | None:
    """If integer polynomial is a square in Q[t], return sqrt coeffs (integer)."""
    # strip leading zeros
    while coeffs and coeffs[-1] == 0:
        coeffs = coeffs[:-1]
    if not coeffs:
        return [0]
    deg = len(coeffs) - 1
    if deg % 2:
        return None
    d = deg // 2
    # leading coeff square
    lc = coeffs[-1]
    s = int(round(math.sqrt(abs(lc))))
    if s * s != abs(lc):
        return None
    if lc < 0:
        return None
    # try integer sqrt by undetermined coefficients, leading s
    from itertools import product

    # bound other coeffs roughly
    bound = max(4, int(abs(coeffs[0]) ** 0.5) + 3, s + 2)
    # too brute for high d
    if d > 2:
        return None
    ranges = [range(-bound, bound + 1) for _ in range(d)]
    for rest in product(*ranges):
        sqrt_c = list(rest) + [s]
        sq = mul_poly(sqrt_c, sqrt_c)
        if pad(sq, len(coeffs)) == pad(coeffs, len(coeffs)):
            return sqrt_c
        sqrt_c[-1] = -s
        sq = mul_poly(sqrt_c, sqrt_c)
        if pad(sq, len(coeffs)) == pad(coeffs, len(coeffs)):
            return sqrt_c
    return None


def pad(a: list[int], n: int) -> list[int]:
    return a + [0] * (n - len(a))


def mul_poly(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def add_poly(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    a, b = pad(a, n), pad(b, n)
    return [x + y for x, y in zip(a, b)]


def scale_poly(a: list[int], s: int) -> list[int]:
    return [s * x for x in a]


def try_linear_grid(k: int, bound: int) -> None:
    """s_ij = p_i t + q_ij with q depending only as a_i + b_j fails; try s_ij = a_i t + b_j."""
    # For k=2, search small a_i, b_j
    if k != 2:
        print("linear grid search only implemented for k=2")
        return
    hits = 0
    for a1, a2, b1, b2 in itertools.product(range(-bound, bound + 1), repeat=4):
        if a1 == a2 and b1 == b2:
            continue
        s11 = [b1, a1]
        s12 = [b2, a1]
        s21 = [b1, a2]
        s22 = [b2, a2]
        # need s11^2 - s12^2 independent of... wait we need
        # s11^2 - d1^2 = s12^2 - d2^2 so d^2 not polynomials here.
        # Check rectangle: s11^2 + s22^2 - s12^2 - s21^2 == 0
        left = add_poly(mul_poly(s11, s11), mul_poly(s22, s22))
        right = add_poly(mul_poly(s12, s12), mul_poly(s21, s21))
        n = max(len(left), len(right))
        if pad(left, n) == pad(right, n):
            # mixed term 2(a1-a2)(b1-b2) t from expanding (a t+b)^2
            hits += 1
            print("rectangle hit", a1, a2, b1, b2)
            if hits >= 5:
                break
    print("done linear k=2 hits", hits)


if __name__ == "__main__":
    try_linear_grid(2, 5)
    # Document: (a_i t + b_j)^2 has mixed term 2 a_i b_j t, rectangle fails unless a_i const or b_j const.
