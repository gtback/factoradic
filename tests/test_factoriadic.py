# SPDX-FileCopyrightText: 2023 Greg Back <git@gregback.net>
# SPDX-License-Identifier: MIT

import pytest

from factoradic import MAX_FACTORADIC, factoradic_to_int, int_to_factoradic

test_data = {
    1: "1",
    2: "10",
    3: "11",
    4: "20",
    5: "21",
    6: "100",
    7: "101",
    24: "1000",
    25: "1001",
    5038: "654320",
    5039: "654321",
    5040: "1000000",
    999998: "266251210",
    999999: "266251211",
    1000000: "266251220",
    1000001: "266251221",
}

@pytest.mark.parametrize("i,f", test_data.items())
def test_itof(i, f):
    assert int_to_factoradic(i) == f

@pytest.mark.parametrize("f,i", ((v, k) for (k, v) in test_data.items()))
def test_ftoi(f, i):
    assert factoradic_to_int(f) == i

def test_invalid_ftoi():
    with pytest.raises(ValueError):
        factoradic_to_int("2")

def test_max_factoradic():
    assert factoradic_to_int("987654321") == MAX_FACTORADIC

def test_int_too_large():
    with pytest.raises(ValueError):
        int_to_factoradic(MAX_FACTORADIC + 1)

def test_zero():
    assert int_to_factoradic(0) == "0"
    assert factoradic_to_int("0") == 0

def test_negative_int():
    with pytest.raises(ValueError):
        int_to_factoradic(-1)
