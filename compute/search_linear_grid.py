#!/usr/bin/env python3
"""Search for 3x3 grids with d_j and s_ij linear in one parameter.

For linear forms d=p*t+q and s=r*t+u, the row value

    A = s^2-d^2 = 4*N

is represented by its three coefficients.  A K_{3,3} in the resulting
bipartite graph (row quadratics versus difference forms) is exactly a
3x3 polynomial identity of this restricted degree.
"""

from __future__ import annotations

import argparse
import itertools
from collections import defaultdict

Linear = tuple[int, int]
Quadratic = tuple[int, int, int]


def canonical_linear(form: Linear) -> Linear:
    """Identify a linear form with its negative."""
    p, q = form
    if p < 0 or (p == 0 and q < 0):
        return -p, -q
    return form


def difference_of_squares(s: Linear, d: Linear) -> Quadratic:
    r, u = s
    p, q = d
    return r * r - p * p, 2 * (r * u - p * q), u * u - q * q


def find_grids(bound: int, limit: int) -> list[tuple[tuple[Linear, ...], tuple[Quadratic, ...]]]:
    forms = {
        canonical_linear((p, q))
        for p in range(-bound, bound + 1)
        for q in range(-bound, bound + 1)
        if (p, q) != (0, 0)
    }

    rows_to_differences: dict[Quadratic, set[Linear]] = defaultdict(set)
    for d in forms:
        for s in forms:
            row = difference_of_squares(s, d)
            if row != (0, 0, 0):
                rows_to_differences[row].add(d)

    triple_to_rows: dict[tuple[Linear, Linear, Linear], list[Quadratic]] = defaultdict(list)
    for row, differences in rows_to_differences.items():
        if len(differences) < 3:
            continue
        for triple in itertools.combinations(sorted(differences), 3):
            bucket = triple_to_rows[triple]
            if len(bucket) < 3:
                bucket.append(row)

    hits = []
    for differences, rows in triple_to_rows.items():
        if len(rows) >= 3:
            # Remove constant/homothetic grids: at least two row quadratics
            # must not be rational scalar multiples.
            if all(
                rows[0][i] * rows[j][0] == rows[j][i] * rows[0][0]
                for j in range(1, 3)
                for i in range(3)
            ):
                continue
            hits.append((differences, tuple(rows[:3])))
            if len(hits) >= limit:
                break
    return hits


def square_root(row: Quadratic, difference: Linear, bound: int) -> Linear | None:
    forms = {
        canonical_linear((p, q))
        for p in range(-bound, bound + 1)
        for q in range(-bound, bound + 1)
        if (p, q) != (0, 0)
    }
    for s in forms:
        if difference_of_squares(s, difference) == row:
            return s
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=8)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    hits = find_grids(args.bound, args.limit)
    print(f"found {len(hits)} grids")
    for differences, rows in hits:
        print("differences", differences)
        print("rows", rows)
        for row in rows:
            print(" square roots", [square_root(row, d, args.bound) for d in differences])


if __name__ == "__main__":
    main()
