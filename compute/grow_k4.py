#!/usr/bin/env python3
"""Grow 4-difference pairs to 3 and 4 integers."""

from __future__ import annotations

from factor_diff import D, _is_square


def n_from(s: int, d: int) -> int | None:
    val = s * s - d * d
    if val <= 0 or val % 4:
        return None
    return val // 4


def all_n_with_diffs(ds: list[int], s_bound: int) -> list[int]:
    d0 = min(ds)
    start = d0 + 2
    if start % 2 != d0 % 2:
        start += 1
    found = []
    for s in range(start, s_bound + 1, 2):
        n = n_from(s, d0)
        if n is None:
            continue
        if all(_is_square(4 * n + d * d) for d in ds if d != d0):
            found.append(n)
    return found


def main() -> None:
    limit = 30000
    min_d = 6
    pool = []
    for n in range(1, limit + 1):
        d = D(n)
        if len(d) >= min_d:
            pool.append((n, d))
    print("pool", len(pool), flush=True)
    pairs = []
    for i, (n1, d1) in enumerate(pool):
        for n2, d2 in pool[i + 1 :]:
            inter = d1 & d2
            if len(inter) >= 4:
                pairs.append((n1, n2, tuple(sorted(inter)[:8])))
    print("pairs", len(pairs), flush=True)
    best = []
    for n1, n2, inter in pairs[:400]:
        ds = list(inter[:4])
        s_bound = min(8000, int((4 * max(n1, n2) + ds[0] ** 2) ** 0.5) + 2000)
        ns = all_n_with_diffs(ds, s_bound)
        if len(ns) >= 3:
            best.append((ns, ds))
            print(">=3 n", ns, "diffs", ds, flush=True)
        if len(ns) >= 4:
            print("K4 CANDIDATE", ns, ds, flush=True)
    print("triples-or-better", len(best))


if __name__ == "__main__":
    main()
