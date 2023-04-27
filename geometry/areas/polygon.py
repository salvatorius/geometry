from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from geometry.points import Point2D, AnyPoint

CoordsTuple = Tuple[NDArray[np.float32],NDArray[np.float32]]

class Polygon:
    @staticmethod
    def _is_valid_tuple(obj) -> bool:
        return isinstance(obj, tuple) \
            and len(obj) == 2 \
            and all(isinstance(value, (int, float)) for value in obj)

    def __init__(self, points: List[AnyPoint]):
        vertices = []
        for point in points:
            if isinstance(point, Point2D):
                vertices.append((point.x, point.y))
            elif Polygon._is_valid_tuple(point):
                vertices.append(point)
            else:
                raise TypeError(f"Expected tuple of 2 floats or Point2D, got {type(point)}")
        self._vertices = np.array(vertices)

    @property
    def n(self) -> int:
        return self._vertices.shape[0]

    @property
    def points(self) -> List[Point2D]:
        return [Point2D(x, y) for x, y in self._vertices]

    @property
    # extract x and y values using array indexing
    def coordinates(self) -> CoordsTuple:
        return self._vertices[:, 0], self._vertices[:, 1]

    def calc_area(self) -> float:
        # Shift the vertices so that v[i] is paired with v[i+1] in the dot product
        v_shifted = np.roll(self._vertices, -1, axis=0)

        # Compute the cross product of each pair of adjacent vertices
        cross_product = np.cross(self._vertices, v_shifted)

        # Compute the area of the polygon as half the sum of the cross products
        return abs(0.5 * np.sum(cross_product))

    def __repr__(self):
        return f'Polygon <{self.n} vertices polygon>'
