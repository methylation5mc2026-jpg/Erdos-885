#!/usr/bin/env python3
"""Verify Choudhry's numerical tables and search for admissible square translates.

For a table normalized by B_1=0, a rational translate T=(x/q)^2 turns the
square side into squares precisely when

    y_j^2 - x^2 = q^2 B_j.

It yields positive integers for Erdos 885 only if x^2 < q^2 min(A).  The
search below is exhaustive for reduced denominators 1 <= q <= the bound:
factor pairs of q^2 B_2 enumerate every possible x for the first equation.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt
from typing import Any


TABLES: dict[str, dict[str, Any]] = {
    "choudhry_5x3_theorem_2": {
        "source": "arXiv:2508.07806, Theorem 2 numerical example",
        "A": [198916, 532900, 1674436, 13468900, 19404025],
        "B": [0, 3588000, 8527200],
    },
    "choudhry_4x4_theorem_3": {
        "source": "arXiv:2508.07806, Theorem 3 numerical example",
        "A": [44782864, 340218025, 1738222864, 2777290000],
        "B": [0, 25777136, 1222007600, 1719217136],
    },
    "choudhry_4x4_theorem_4": {
        "source": "arXiv:2508.07806, Theorem 4 numerical example",
        "A": [14400, 266256, 435600, 12110400],
        "B": [0, 104625, 223744, 12096000],
    },
    "lagrange_4x4_cited_by_choudhry": {
        "source": "older Lagrange example quoted in arXiv:2508.07806, section 1",
        "A": [324, 54756, 119716, 264196],
        "B": [0, 79200, 227205, 1258560],
    },
}


def square_root(value: int) -> int | None:
    if value < 0:
        return None
    root = isqrt(value)
    return root if root * root == value else None


def factor_integer(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime += 1 if prime == 2 else 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def divisors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for prime, exponent in factors.items():
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return result


def smallest_prime_factors(bound: int) -> list[int]:
    spf = list(range(bound + 1))
    for prime in range(2, isqrt(bound) + 1):
        if spf[prime] != prime:
            continue
        for value in range(prime * prime, bound + 1, prime):
            if spf[value] == value:
                spf[value] = prime
    return spf


def factor_from_spf(value: int, spf: list[int]) -> dict[int, int]:
    factors: dict[int, int] = {}
    while value > 1:
        prime = spf[value]
        factors[prime] = factors.get(prime, 0) + 1
        value //= prime
    return factors


def search_admissible_translate(
    A: list[int],
    B: list[int],
    denominator_bound: int,
    spf: list[int],
) -> dict[str, Any]:
    """Search 0 < (x/q)^2 < min(A), with x/q reduced."""
    first_offset = next(offset for offset in B if offset > 0)
    offset_factors = factor_integer(first_offset)
    candidate_count = 0

    for q in range(1, denominator_bound + 1):
        factors = offset_factors.copy()
        for prime, exponent in factor_from_spf(q, spf).items():
            factors[prime] = factors.get(prime, 0) + 2 * exponent

        product = q * q * first_offset
        for lower_factor in divisors(factors):
            if lower_factor * lower_factor > product:
                continue
            upper_factor = product // lower_factor
            if (lower_factor + upper_factor) % 2:
                continue
            x = (upper_factor - lower_factor) // 2
            if x <= 0 or gcd(x, q) != 1:
                continue
            if x * x >= q * q * min(A):
                continue
            candidate_count += 1

            roots = []
            for offset in B:
                root = square_root(x * x + q * q * offset)
                if root is None:
                    break
                roots.append(root)
            else:
                return {
                    "found": True,
                    "reduced_denominator_bound": denominator_bound,
                    "candidates_tested": candidate_count,
                    "q": q,
                    "x": x,
                    "translate": f"{x * x}/{q * q}",
                    "scaled_square_roots": roots,
                }

    return {
        "found": False,
        "reduced_denominator_bound": denominator_bound,
        "candidates_tested": candidate_count,
    }


def check_table(
    table: dict[str, Any],
    denominator_bound: int,
    spf: list[int],
) -> dict[str, Any]:
    A = table["A"]
    B = table["B"]
    root_matrix: list[list[int]] = []
    for a in A:
        row = []
        for b in B:
            root = square_root(a + b)
            if root is None:
                raise AssertionError(f"{a} + {b} is not a square")
            row.append(root)
        root_matrix.append(row)

    minimum_a = min(A)
    minimum_row = A.index(minimum_a)
    boundary_roots = root_matrix[minimum_row]
    return {
        **table,
        "verified": True,
        "root_matrix": root_matrix,
        "B_itself_all_squares": all(square_root(b) is not None for b in B),
        "automatic_boundary_translate": {
            "t": minimum_a,
            "square_roots_of_B_plus_t": boundary_roots,
            "A_minus_t": [a - minimum_a for a in A],
            "why_not_885": "one transformed row constant is zero",
        },
        "admissible_translate_search": search_admissible_translate(
            A,
            B,
            denominator_bound,
            spf,
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--denominator-bound", type=int, default=20000)
    args = parser.parse_args()
    if args.denominator_bound < 1:
        parser.error("--denominator-bound must be positive")

    spf = smallest_prime_factors(args.denominator_bound)
    result = {
        name: check_table(table, args.denominator_bound, spf)
        for name, table in TABLES.items()
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
