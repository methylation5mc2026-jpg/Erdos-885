#!/usr/bin/env python3
"""Find 3-difference tuples with many n, then inspect extra common diffs."""

from __future__ import annotations

import math
import sys

from factor_diff import D, _is_square, common_differences


def divisors(n: int) -> list[int]:
    n = abs(int(n))
    divs = []
    r = int(math.isqrt(n))
    for i in range(1, r + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return divs


def all_n_sharing(ds: list[int]) -> list[int]:
    d1, d2 = ds[0], ds[1]
    c = d2 * d2 - d1 * d1
    found: set[int] = set()
    for m1 in divisors(c):
        for mm in (m1, -m1):
            if mm == 0 or c % mm:
                continue
            m2 = c // mm
            if (mm + m2) % 2:
                continue
            s1 = (m2 - mm) // 2
            if s1 <= 0:
                continue
            val = s1 * s1 - d1 * d1
            if val <= 0 or val % 4:
                continue
            n = val // 4
            if all(_is_square(4 * n + d * d) for d in ds[1:]):
                found.add(n)
    return sorted(found)


def main() -> None:
    limit = 8000
    pool = []
    for n in range(1, limit + 1):
        d = D(n)
        if len(d) >= 4:
            pool.append((n, d))
    print("pool", len(pool), flush=True)
    seen = set()
    records = []
    for i, (n1, d1) in enumerate(pool):
        for n2, d2 in pool[i + 1 :]:
            inter = d1 & d2
            if len(inter) < 3:
                continue
            ds = tuple(sorted(inter)[:3])
            if ds in seen:
                continue
            seen.add(ds)
            ns = all_n_sharing(list(ds))
            if len(ns) >= 4:
                extra = common_differences(ns[:4])
                records.append((ns, ds, extra))
                print(
                    "many n",
                    len(ns),
                    "on",
                    ds,
                    "first n",
                    ns[:6],
                    "inter4",
                    sorted(extra),
                    flush=True,
                )
                if len(extra) >= 4 and len(ns) >= 4:
                    print("K4 FROM 3-DIFF KERNEL", ns[:4], sorted(extra))
    print("3-diff tuples checked", len(seen), "with >=4 n", len(records))


if __name__ == "__main__":
    main()
