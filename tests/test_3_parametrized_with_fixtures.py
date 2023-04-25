from dataclasses import dataclass
from typing import List, Tuple
from pytest import mark
from geometry.areas.polygon import Polygon, Point2D


@dataclass
class CoordsArea:
    points: List[Tuple[float, float]]
    area: float

FIRST = CoordsArea([(0, 1), (1, 2), (2, 2), (3, 1)], 2)
SECOND = CoordsArea([(0, 3), (1, 3), (2, 2), (3, 2), (2, 1), (1, 1)], 3)
STAR = CoordsArea([
        (6, 3),
        (7, 5),
        (9, 5),
        (7.5, 6.5),
        (8, 9),
        (6, 7.5),
        (4, 9),
        (4.5, 6.5),
        (3, 5),
        (5, 5),
    ],
    14.5
)
MOCK_POLYGONS = [(p.points, p.area) for p in [FIRST, SECOND, STAR]]

@mark.parametrize("coordinates,expected_area", MOCK_POLYGONS)
def test_calc_polygon_area_given_its_points_from_fixture(coordinates, expected_area):
    points = [Point2D(x, y) for x, y in coordinates]
    polygon = Polygon(points)
    assert polygon.calc_area() == expected_area
