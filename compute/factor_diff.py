#!/usr/bin/env python3
"""Factor-difference utilities and checks for Erdős 885."""

from __future__ import annotations

import math
from functools import lru_cache


def factor_pairs(n: int) -> list[tuple[int, int]]:
    if n <= 0:
        raise ValueError("n must be positive")
    pairs = []
    r = int(math.isqrt(n))
    for a in range(1, r + 1):
        if n % a == 0:
            pairs.append((a, n // a))
    return pairs


def D(n: int) -> set[int]:
    return {abs(a - b) for a, b in factor_pairs(n)}


def d_in_D(n: int, d: int) -> bool:
    return (4 * n + d * d).is_square() if hasattr(int, "is_square") else _is_square(4 * n + d * d)


def _is_square(m: int) -> bool:
    if m < 0:
        return False
    r = math.isqrt(m)
    return r * r == m


def common_differences(ns: list[int]) -> set[int]:
    acc = D(ns[0])
    for n in ns[1:]:
        acc &= D(n)
    return acc


def verify_matrix(ns: list[int], ds: list[int]) -> bool:
    for n in ns:
        for d in ds:
            if not _is_square(4 * n + d * d):
                return False
    return True


@lru_cache(maxsize=None)
def D_cached(n: int) -> frozenset[int]:
    return frozenset(D(n))


GUIDULI_1_DIFFS = [420, 3780, 14940, 76860]
GUIDULI_1_NS = [6925500, 37901500, 108448956]
GUIDULI_2_DIFFS = [420, 3780, 61695, 154332]
GUIDULI_2_NS = [2778300, 862552800, 5400442044]
MAUSBERG_NS = [79200, 227205, 1258560]
MAUSBERG_DIFFS = [36, 468, 692, 1028]


def check_guiduli() -> None:
    c1 = common_differences(GUIDULI_1_NS)
    c2 = common_differences(GUIDULI_2_NS)
    cm = common_differences(MAUSBERG_NS)
    print("Guiduli1 intersection size", len(c1), "contains listed diffs", set(GUIDULI_1_DIFFS) <= c1)
    print("Guiduli1 listed subset ok", set(GUIDULI_1_DIFFS) <= c1, "full", sorted(c1))
    print("Guiduli2 listed subset ok", set(GUIDULI_2_DIFFS) <= c2, "full", sorted(c2)[:40], "card", len(c2))
    print("Mausberg intersection", sorted(cm), "eq listed", cm == set(MAUSBERG_DIFFS))


if __name__ == "__main__":
    check_guiduli()
