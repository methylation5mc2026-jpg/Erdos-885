#!/usr/bin/env python3
"""Exact bounded searches for 5x5 additive-square tables.

Two searches use the same finite incidence graph.  An edge (u, c) means that
u^2 + c is a square v^2 with 1 <= u < v <= the requested root bound.

* unrestricted: find five u's incident to four positive c's; c=0 supplies
  the fifth column;
* square-side: reinterpret u as a positive difference d and c as a positive
  row constant A.  A K_{5,5} gives A_i + d_j^2 square.

The latter can be scaled to Erdos 885 by replacing (A, d, s) with
(4A, 2d, 2s), so no congruence condition on A is needed in this search.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import combinations
from math import isqrt
from pathlib import Path
from time import perf_counter
from typing import Any


def build_columns(bound: int, minimum_support: int) -> tuple[int, list[tuple[int, tuple[int, ...]]]]:
    """Return labels and supports for c=v^2-u^2, with 1 <= u < v <= bound."""
    supports: dict[int, list[int]] = defaultdict(list)
    for v in range(2, bound + 1):
        vv = v * v
        for u in range(1, v):
            supports[vv - u * u].append(u)

    column_count = len(supports)
    columns = [
        (label, tuple(sorted(rows)))
        for label, rows in supports.items()
        if len(rows) >= minimum_support
    ]
    columns.sort()
    return column_count, columns


def find_biclique(
    columns: list[tuple[int, tuple[int, ...]]],
    row_bound: int,
    left_size: int,
    right_size: int,
) -> dict[str, Any]:
    """Find K_(left_size,right_size), exhaustively, by frequent-itemset mining."""
    row_columns: list[set[int]] = [set() for _ in range(row_bound + 1)]
    supports: list[tuple[int, ...]] = []
    labels: list[int] = []
    for column_id, (label, rows) in enumerate(columns):
        labels.append(label)
        supports.append(rows)
        for row in rows:
            row_columns[row].add(column_id)

    # Every extension with right_size common columns starts with a pair that
    # occurs together in at least right_size columns.  Counting those pairs
    # avoids scanning all O(row_bound^2) pairs of large bit vectors.
    pair_counts: dict[tuple[int, int], int] = defaultdict(int)
    for rows in supports:
        for pair in combinations(rows, 2):
            pair_counts[pair] += 1

    frequent_pairs = [
        (pair, count) for pair, count in pair_counts.items() if count >= right_size
    ]
    frequent_pairs.sort()

    max_common_by_depth = [0] * (left_size + 1)
    witness_by_depth: list[dict[str, Any] | None] = [None] * (left_size + 1)
    deepest = 0

    def record(chosen: tuple[int, ...], common: set[int]) -> None:
        nonlocal deepest
        depth = len(chosen)
        count = len(common)
        deepest = max(deepest, depth)
        if count > max_common_by_depth[depth]:
            max_common_by_depth[depth] = count
            witness_by_depth[depth] = {
                "rows": list(chosen),
                "columns": [labels[column_id] for column_id in sorted(common)],
            }

    def extend(chosen: tuple[int, ...], common: set[int]) -> tuple[tuple[int, ...], set[int]] | None:
        record(chosen, common)
        if len(chosen) == left_size:
            return chosen, common

        last = chosen[-1]
        candidate_counts: dict[int, int] = defaultdict(int)
        for column_id in common:
            for row in supports[column_id]:
                if row > last:
                    candidate_counts[row] += 1

        for row in sorted(candidate_counts):
            if candidate_counts[row] < right_size:
                continue
            next_common = common & row_columns[row]
            if len(next_common) < right_size:
                continue
            hit = extend(chosen + (row,), next_common)
            if hit is not None:
                return hit
        return None

    hit: tuple[tuple[int, ...], set[int]] | None = None
    for (first, second), _count in frequent_pairs:
        common = row_columns[first] & row_columns[second]
        hit = extend((first, second), common)
        if hit is not None:
            break

    result: dict[str, Any] = {
        "target": {"left_rows": left_size, "right_columns": right_size},
        "eligible_columns": len(columns),
        "frequent_pairs": len(frequent_pairs),
        "found": hit is not None,
        "deepest_frequent_row_set": deepest,
        "max_common_columns_by_depth": {
            str(depth): count
            for depth, count in enumerate(max_common_by_depth)
            if depth >= 2 and count
        },
        "witnesses_by_depth": {
            str(depth): witness
            for depth, witness in enumerate(witness_by_depth)
            if depth >= 2 and witness is not None
        },
    }
    if hit is not None:
        rows, common = hit
        selected_columns = sorted(common, key=lambda column_id: labels[column_id])[:right_size]
        result["rows"] = list(rows)
        result["columns"] = [labels[column_id] for column_id in selected_columns]
    return result


def add_table_data(result: dict[str, Any], square_side: bool) -> None:
    """Attach A, B, and square-root matrices when a biclique was found."""
    if not result["found"]:
        return
    rows = result["rows"]
    columns = result["columns"]
    if square_side:
        result["A"] = columns
        result["B"] = [row * row for row in rows]
        result["root_matrix"] = [
            [isqrt(a + d * d) for d in rows]
            for a in columns
        ]
    else:
        result["A"] = [row * row for row in rows]
        result["B"] = [0] + columns
        result["root_matrix"] = [
            [row] + [isqrt(row * row + column) for column in columns]
            for row in rows
        ]


def run(bound: int) -> dict[str, Any]:
    started = perf_counter()
    total_columns, columns = build_columns(bound, minimum_support=5)
    built_at = perf_counter()

    unrestricted = find_biclique(
        columns,
        row_bound=bound,
        left_size=5,
        right_size=4,
    )
    unrestricted_at = perf_counter()
    add_table_data(unrestricted, square_side=False)

    square_side = find_biclique(
        columns,
        row_bound=bound,
        left_size=5,
        right_size=5,
    )
    finished = perf_counter()
    add_table_data(square_side, square_side=True)

    return {
        "root_bound": bound,
        "domain": {
            "unrestricted": (
                "B_1=0, B_j>0, and every cell root is in [1, root_bound]"
            ),
            "square_side": (
                "A_i>0, d_j>0, and every d_j and cell root is in [1, root_bound]"
            ),
        },
        "incidence": {
            "all_positive_labels": total_columns,
            "labels_with_support_at_least_5": len(columns),
        },
        "unrestricted_5x5": unrestricted,
        "square_side_5x5": square_side,
        "elapsed_seconds": {
            "build": round(built_at - started, 6),
            "unrestricted": round(unrestricted_at - built_at, 6),
            "square_side": round(finished - unrestricted_at, 6),
            "total": round(finished - started, 6),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=1000)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.bound < 5:
        parser.error("--bound must be at least 5")

    result = run(args.bound)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json is not None:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
