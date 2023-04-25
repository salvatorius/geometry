from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

from geometry.points import Point2D

@dataclass
class Polygon:
    vertices: List[Point2D]

    @property
    def n(self) -> int:
        return len(self.vertices)

    def calc_area(self) -> float:
        # Convert vertices to a 2D Numpy array
        vs = np.array([(p.x, p.y) for p in self.vertices])

        # Shift the vertices so that v[i] is paired with v[i+1] in the dot product
        v_shifted = np.roll(vs, -1, axis=0)

        # Compute the cross product of each pair of adjacent vertices
        cross_product = np.cross(vs, v_shifted)

        # Compute the area of the polygon as half the sum of the cross products
        return abs(0.5 * np.sum(cross_product))

    @classmethod
    def of(cls, points: List[Tuple[float, float]]) -> 'Polygon':
        return cls(Point2D(x, y) for x, y in points)

    def __repr__(self):
        return f'Polygon <{self.n} vertices polygon>'
