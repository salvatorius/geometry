from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from geometry import Point2D, PointList, is_valid_point_set

NPCoordsTuple = Tuple[NDArray[np.float32],NDArray[np.float32]]

class Polygon:
    def __init__(self, *points: PointList, precision=None, **kwargs):
        left = points[0] if len(points) == 1 else None
        values = left if is_valid_point_set(left) else points
        vertices = [Point2D(point).tuple for point in values]
        self._precision = precision
        self._vertices = np.array(vertices)

    @property
    def n(self) -> int:
        return self._vertices.shape[0]

    @property
    def points(self) -> List[Point2D]:
        return [Point2D(float(x), float(y)) for x, y in self._vertices]

    @property
    # extract x and y values using array indexing
    def coordinates(self) -> NPCoordsTuple:
        return self._vertices[:, 0], self._vertices[:, 1]

    def calc_area(self) -> float:
        # Shift the vertices so that v[i] is paired with v[i+1] in the dot product
        v_shifted = np.roll(self._vertices, -1, axis=0)

        # Compute the cross product of each pair of adjacent vertices
        cross_product = np.cross(self._vertices, v_shifted)

        # Compute the area of the polygon as half the sum of the cross products
        return abs(0.5 * np.sum(cross_product))

    def __repr__(self):
        return f'Polygon [{self.n} vertices polygon]'
