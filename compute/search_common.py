#!/usr/bin/env python3
"""Search for extra integers sharing a prescribed set of factor differences."""

from __future__ import annotations

import math
import sys
from itertools import combinations

from factor_diff import (
    D,
    GUIDULI_1_DIFFS,
    GUIDULI_1_NS,
    GUIDULI_2_DIFFS,
    GUIDULI_2_NS,
    MAUSBERG_DIFFS,
    MAUSBERG_NS,
    _is_square,
    common_differences,
)


def n_from_square_and_diff(s: int, d: int) -> int | None:
    val = s * s - d * d
    if val <= 0 or val % 4:
        return None
    return val // 4


def search_n_with_differences(ds: list[int], s_bound: int) -> list[int]:
    """Enumerate s such that s^2 - d0^2 is 4N > 0 and all other 4N+d^2 are squares."""
    d0 = ds[0]
    found = []
    # s > d0, s ≡ d0 (mod 2)
    start = d0 + 2 if (d0 % 2 == 0) else d0 + 1
    if start % 2 != d0 % 2:
        start += 1
    for s in range(start, s_bound + 1, 2):
        n = n_from_square_and_diff(s, d0)
        if n is None:
            continue
        if all(_is_square(4 * n + d * d) for d in ds[1:]):
            found.append(n)
    return found


def divisor_rich_search(limit_n: int, min_divisors: int, k: int) -> list[tuple[list[int], list[int]]]:
    """Among n <= limit with many divisors, look for k-tuples with |intersection D| >= k."""
    pool = []
    for n in range(1, limit_n + 1):
        diffs = D(n)
        if len(diffs) >= min_divisors:
            pool.append((n, diffs))
    print(f"pool size {len(pool)} with |D| >= {min_divisors} and n <= {limit_n}", flush=True)
    # invert: each difference -> ns
    inv: dict[int, list[int]] = {}
    dset: dict[int, set[int]] = {}
    for n, diffs in pool:
        dset[n] = diffs
        for d in diffs:
            inv.setdefault(d, []).append(n)
    # differences that hit at least k numbers in the pool
    frequent = {d: ns for d, ns in inv.items() if len(ns) >= k}
    print(f"frequent diffs {len(frequent)}", flush=True)
    hits = []
    seen = set()
    # brute k-subsets of pool only among numbers sharing a frequent diff
    candidates = sorted({n for ns in frequent.values() for n in ns})
    print(f"candidates {len(candidates)}", flush=True)
    if len(candidates) > 80:
        # too large for naive k-subsets; instead grow from pairs
        return greedy_grow(candidates, dset, k)
    for tup in combinations(candidates, k):
        inter = dset[tup[0]]
        for n in tup[1:]:
            inter = inter & dset[n]
            if len(inter) < k:
                break
        if len(inter) >= k:
            key = tuple(sorted(tup))
            if key not in seen:
                seen.add(key)
                hits.append((list(tup), sorted(inter)))
    return hits


def greedy_grow(candidates: list[int], dset: dict[int, set[int]], k: int) -> list[tuple[list[int], list[int]]]:
    hits = []
    seen = set()
    m = min(len(candidates), 120)
    for i in range(m):
        for j in range(i + 1, m):
            inter = dset[candidates[i]] & dset[candidates[j]]
            if len(inter) < k:
                continue
            group = [candidates[i], candidates[j]]
            cur = inter
            for n in candidates:
                if n in group:
                    continue
                new = cur & dset[n]
                if len(new) >= k:
                    group.append(n)
                    cur = new
                if len(group) >= k and len(cur) >= k:
                    key = (tuple(sorted(group[:k])), tuple(sorted(cur)))
                    if key not in seen:
                        seen.add(key)
                        hits.append((sorted(group[:k]), sorted(cur)))
                    break
    return hits


def extra_around_guiduli() -> None:
    for name, ds, known in [
        ("Guiduli1", GUIDULI_1_DIFFS, GUIDULI_1_NS),
        ("Guiduli2", GUIDULI_2_DIFFS, GUIDULI_2_NS),
        ("Mausberg", MAUSBERG_DIFFS, MAUSBERG_NS),
    ]:
        print(f"\n=== {name} prescribed diffs {ds} known n {known} ===", flush=True)
        bound = max(int(math.sqrt(4 * max(known) + ds[0] ** 2)) + 1, ds[0] + 2) * 4
        bound = min(bound, 2_000_000)
        found = search_n_with_differences(ds, bound)
        print(f"search s <= {bound}: found {len(found)} n's")
        print("found includes known", set(known) <= set(found))
        extra = [n for n in found if n not in known]
        print("extra n", extra[:20], "count", len(extra))
        if len(found) >= 5:
            print("at least 5 n sharing these 4 diffs")


if __name__ == "__main__":
    extra_around_guiduli()
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    hits = divisor_rich_search(limit, min_divisors=k, k=k)
    print(f"\nhits for k={k} n<={limit}: {len(hits)}")
    for ns, ds in hits[:15]:
        print(ns, "inter", ds[:12], "card", len(ds))
