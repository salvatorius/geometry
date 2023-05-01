from typing import List, Tuple
from dataclasses import dataclass
import pytest

from geometry import Polygon

@dataclass
class ParamTestCase:
    points: List[Tuple]
    area: float = 1

TestCases = List[ParamTestCase]

@pytest.fixture
def polygons() -> TestCases:
    return [
        # Isosceles Triangle
        ParamTestCase(points=[(0, 3), (4, -1), (-4, -1)], area = 16),
        # Equilateral Triangle
        ParamTestCase(points=[(-3, 0), (1.31, 4.08), (2.69, -1.69)], area = 15.2495),
        # Square 1
        ParamTestCase(points=[(1, 4), (3, 0), (-1, -2), (-3, -2)], area = 16),
        # Square 2
        ParamTestCase(points=[(0,2), (2,1), (1,-1), (0,-1)], area = 4),
        # Diamond
        ParamTestCase(points=[(0.5,2.5),(2.5,-0.5),(0.5,-3.5),(-1.5,-0.5)], area = 12),
        # Trapeze
        ParamTestCase(points=[(0, 2), (1, 0), (-1, -3), (-3, 1)], area = 10.5),
        # Parallelogram
        ParamTestCase(points=[(0,4),(2,0),(1,-3),(-1,1)], area = 10),
        # Pentagon
        ParamTestCase(points=[(-1,-1),(1.85,-0.07),(1.85,2.93),(-1.01,3.85),(-2.77,1.42)], area = 15.486),
        # Heptagon
        ParamTestCase(points=[(1,-2),(-1.1,-2.3),(-2.64,-0.84),(-2.46,1.27),(-0.7,2.45),(1.32,1.81),(2.08,-0.17)], area = 16.3427),
        # Bird
        ParamTestCase(points=[(0, 3), (1, 3), (2, 2), (3, 2), (2, 1), (1, 1)], area = 3),
        # Star
        ParamTestCase(points=[(6, 3),(7, 5),(9, 5),(7.5, 6.5),(8, 9),(6, 7.5),(4, 9),(4.5, 6.5),(3, 5),(5, 5)], area = 14.5),
        # Crown
        ParamTestCase(points=[(-4,-2),(-6,3),(-4,1),(-3,3),(-2,1),(-1,3),(0,1),(1,3),(2,1),(3,3),(4,1),(6,3),(4,-2)], area=38)
        # ...
    ]

CASE_COUNT = 12

@pytest.mark.parametrize("index", range(CASE_COUNT))
def test_calc_polygon_area_given_its_points_from_fixture_list_item_by_index(polygons, index):
    # Picking our particular test case for this run
    # by index from the "polygons" fixture
    test_case = polygons[index]
    polygon = Polygon(test_case.points)
    assert polygon.calc_area() == pytest.approx(test_case.area, 1e-04)
