from pytest import mark
from geometry.areas.polygon import Polygon, Point2D

@mark.parametrize("coordinates,expected_area", [
    ([(0,1),(1,2),(2,2),(3,1)], 2),
    ([(0,3),(1,3),(2,2),(3,2),(2,1),(1,1)], 3),
    ([(6,3),(7,5),(9,5),(7.5,6.5),(8,9),(6,7.5),(4,9),(4.5,6.5),(3,5),(5,5)], 14.5)
])
def test_calc_polygon_area_given_its_points_as_coordinate_tuples(coordinates, expected_area):
    points = [Point2D(x, y) for x, y in coordinates]
    polygon = Polygon(points)
    assert polygon.calc_area() == expected_area
