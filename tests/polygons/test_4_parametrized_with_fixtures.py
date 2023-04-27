from pytest import mark, fixture
from geometry.areas.polygon import Polygon


@fixture
def trapeze():
    return [(0, 1), (1, 2), (2, 2), (3, 1)]

@fixture
def bird():
    return [(0, 3), (1, 3), (2, 2), (3, 2), (2, 1), (1, 1)]

@fixture
def star():
    return [(6, 3),(7, 5),(9, 5),(7.5, 6.5),(8, 9),(6, 7.5),(4, 9),(4.5, 6.5),(3, 5),(5, 5)]


@mark.parametrize("coord_fixture_name,expected_area", [
    ('trapeze', 2),
    ('bird', 3),
    ('star', 14.5)
    ])
def test_calc_polygon_area_given_its_points_from_fixture(coord_fixture_name, expected_area, request):
    points = request.getfixturevalue(coord_fixture_name)
    polygon = Polygon(points)
    assert polygon.calc_area() == expected_area
