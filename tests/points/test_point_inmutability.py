import pytest

from tests.constants import TDD
from geometry import Point2D


def test_inmutability_of_new_points_instanced_from_variables():
    x1, y1 = 3, 5
    source = (x1, y1)
    target = Point2D(source)
    # at this moment, values should remain the same
    assert target.x == source[0] == 3
    assert target.y == source[1] == 5
    # now let's change the original values
    x1, y1 = 35, 70
    # the value change won't affect neither the tuple
    assert (source[0], source[1]) != (35, 70)
    # nor the Point created from that tuple
    assert target.x != 35
    assert target.y != 70
    # the point coordinates still match the original values instead
    assert {target.x, target.y} == {3, 5}
    # replacing the tuple at a whole won't impact the point either
    source = (10, 10)
    assert {target.x, target.y} == {3, 5}


@pytest.mark.xfail(reason=TDD)
def test_inmutability_of_new_points_instanced_from_another_point():
    x1, y1 = 3, 5
    source = Point2D(x1, y1)
    target = Point2D(source)
    # at this moment, values should remain the same
    assert target.x == source.x == 3
    assert target.y == source.y == 5
    # change the original values
    x1, y1 = 35, 70
    # the value change shall not affect
    # neither the source point nor the cloned one
    assert {source.x, source.y} == {3, 5}
    assert {target.x, target.y} == {3, 5}
    # even if we replace the value of
    # the variable we assigned the source point to
    another_point = Point2D(15, 30)
    source = another_point
    assert target.x != source.x
    assert target.y != source.y
    assert target != source
    assert {target.x, target.y} == {3, 5}


@pytest.mark.xfail(reason=TDD)
def test_equality_of_two_distinct_points_with_same_coordinates():
    x, y = 3, 7
    example = Point2D(x, y)
    another = Point2D(3, 7)
    # confirm they're 2 distinct/unique instances
    assert example is not another
    # validate that they're considered as equals
    # since the geometrical points they represent are the same
    assert example.x == another.x
    assert example == another
    # This should be true for integer coordinates
    # even if the numeric types were different at instance time
    asreal = Point2D(3.0, 14e1 / 20)
    assert example == asreal
