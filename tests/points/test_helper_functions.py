from typing import Any
import pytest

from geometry import BasePair, is_numeric, has_numeric_values


@pytest.mark.parametrize("subject", [0, 12, 12.8, 1e-10])
def test_is_numeric_value_function_returns_true(subject):
    assert is_numeric(subject)

@pytest.mark.parametrize("subject", [
    "1",
    True,
    None,
    [1],
    (2,3),
    ])
def test_is_numeric_value_function_returns_false(subject):
    assert not is_numeric(subject)


@pytest.mark.parametrize("subject", [
    (2,3,4),
    [1,2],
    (12e-7, 10/3, .40),
    list(range(10)),
    ])
def test_collection_has_all_numeric_values_function_returns_true(subject):
    assert has_numeric_values(subject)

@pytest.mark.parametrize("subject", [
    1,
    None,
    (2,3,"4"),
    [1,2,None],
    (12e-7, 10/3, .40, "False"),
    range(10),
    ])
def test_collection_has_all_numeric_values_function_returns_false(subject):
    assert not has_numeric_values(subject)

@pytest.mark.parametrize("subject,cap,expected", [
    ([10.0], 2, True),
    ([1,2.0,3/2,"2"], 3, True),
    ([1,2.0,3/2,"2"], 4, False),
])
def test_collection_has_n_count_of_numeric_values_function(subject: Any, cap: int, expected: bool):
    assert has_numeric_values(subject, up_to=cap) == expected

def test_has_numeric_vales_matches_base_pair_subject():
    pair = BasePair(2, 3)
    assert has_numeric_values(pair, up_to=2)
