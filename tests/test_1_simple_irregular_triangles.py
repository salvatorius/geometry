from pytest import mark, fixture
from geometry.areas.polygon import Polygon, Point2D

@fixture
def _3coordinates():
    return [
        (5.0,3.0),
        (0,10.0),
        (1.0,-1.0)
    ]

def test_calc_triangle_area_given_its_3_points(_3coordinates):
    points = [Point2D(x, y) for x, y in _3coordinates]
    triangle = Polygon(points)
    assert triangle.calc_area() == 24

def test_triangle_instanced_from_its_coordinates():
    coordinates = [(1,2), (2,3), (3,4)]
    triangle = Polygon(coordinates)
    assert triangle.n == 3
    assert str(triangle).startswith("Polygon")
    assert "3 vertices" in str(triangle)

# pylint: disable=no-member # justify=TDD
@mark.xfail(reason='TDD [Still Not Implemented]')
def test_triangle_perimeter(_3coordinates):
    triangle = Polygon.of(_3coordinates)
    # todo: implement this perimeter method
    assert triangle.perimeter() == 25.305
