import pytest

from geometry import Point2D


def test_create_point_from_a_proper_pair_of_numbers():
    point = Point2D(2, 3)
    assert point.x, point.y == (2, 3)

def test_create_point_from_another_point():
    source_point = Point2D(5, 15)
    target_point = Point2D(source_point)
    assert target_point.x, target_point.y == (5, 15)

def test_create_point_with_a_single_value():
    point = Point2D(7)
    assert point.x == 0
    assert point.y == 7
    assert (point.x, point.y) == (0, 7)

def test_create_point_from_a_tuple_of_numbers():
    pair = (2, 3)
    point = Point2D(pair)
    assert point.x, point.y == (2, 3)

def test_creating_point_with_any_value_shall_raise_an_exception():
    with pytest.raises(Exception):
        Point2D()

def test_creating_point_with_a_non_numeric_value_shall_raise_an_exception():
    with pytest.raises(Exception):
        Point2D("2, 3")

def test_creating_point_with_more_than_2_values_will_ignore_the_extra_values():
    point = Point2D(3, 5, 12, 0, 14, "extra")
    assert point.x == 3
    assert point.y == 5
