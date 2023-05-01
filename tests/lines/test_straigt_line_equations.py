import pytest

from tests.constants import TDD, WIP

from geometry import Line


def test_straight_line_instanced_from_gradient_and_y_intercept():
    line = Line(gradient = 4, y_intercept = 3)
    assert line.gradient == 4
    assert line.intercept == 3

@pytest.mark.xfail(reason=WIP)
def test_straight_line_instanced_from_two_ordered_pairs():
    line = Line((1, 2), (2, 3))
    assert line.gradient == 1
    assert line.intercept == 1

@pytest.mark.xfail(reason=TDD)
def test_straight_line_instanced_from_gradient_and_an_arbitrary_point():
    line = Line((2,4), gradient=2)
    assert line.gradient == 2
    assert line.intercept == 0

@pytest.mark.xfail(reason=TDD)
def test_intersection_of_lines():
    line1 = Line((3,0), y_intercept=3)
    line2 = Line((2,2), (-2,2))
    assert line1 & line2 == (1, 2)
