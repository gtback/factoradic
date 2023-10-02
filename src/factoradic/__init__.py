# SPDX-FileCopyrightText: 2023 Greg Back <git@gregback.net>
# SPDX-License-Identifier: MIT

import math

MAX_FACTORADIC = 3628799  # == int_to_factoradic("987654321")

# This only supports up to 9 digits in the factoradic representation. A possible
# enhancement would be to start using letters ("A" for 10, "B" for 11, etc.)
thresholds = {x: math.factorial(x) for x in range(1,10)}

def int_to_factoradic(val: int) -> str:
    """Convert a non-negative integer to its factoradic (string) representation"""
    if val >= MAX_FACTORADIC:
        raise ValueError(f"Value {val} too large to represent as factoradic")
    if val < 0:
        # We could just return the factoradic of the negative value with leading "-"
        raise ValueError(f"Value must be non-negative")
    r = ""
    for x in range(9, 0, -1):
        char = val // thresholds[x]
        val = val % thresholds[x]
        r = r + str(char)
    # Remove all leading zeros. If all zeros, return "0"
    return r.lstrip("0") or "0"

def factoradic_to_int(val: str) -> int:
    "Convert a factoradic number (string) to an integer"
    sum = 0
    for (base, v) in enumerate(reversed(val), start=2):
        v = int(v)
        if v >= base:
            raise ValueError(f"Invalid digit {v} for base {base}")
        sum += v * math.factorial(base - 1)
    return sum
