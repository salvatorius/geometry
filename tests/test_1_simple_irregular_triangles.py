from pytest import mark, fixture

from geometry.areas.polygon import Polygon, Point2D, CoordsTuple

@fixture
def triangle_coords_1():
    return [(1,2),(2,3),(3,4)]

@fixture
def triangle_coords_2():
    return [(5.0,3.0),(0,10.0),(1.0,-1.0)]


def test_triangle_instanced_from_its_coordinates(triangle_coords_1):
    triangle = Polygon(triangle_coords_1)
    coords : CoordsTuple = triangle.coordinates
    assert len(coords) == 2
    x, y = coords
    assert x.shape == y.shape == (3,)

    # Number of points (rows of the np.array)
    assert triangle.n == 3

    # Testing the __repr__ function
    assert str(triangle).startswith("Polygon")
    assert "3 vertices" in str(triangle)

def test_calc_triangle_area_given_its_3_points(triangle_coords_2):
    points = [Point2D(x, y) for x, y in triangle_coords_2]
    triangle = Polygon(points)
    assert triangle.calc_area() == 24

# pylint: disable=no-member # justify=TDD
@mark.xfail(reason='TDD [Still Not Implemented]')
def test_triangle_perimeter(_3coordinates):
    triangle = Polygon.of(_3coordinates)
    # todo: implement this perimeter method
    assert triangle.perimeter() == 25.305
