from dataclasses import dataclass
from typing import Tuple, Union

@dataclass
class Point2D:
    x: float
    y: float

    def __repr__(self):
        return f'Point2D<{self.x},{self.y}>'


OrderedPair = Tuple[float, float]
AnyPoint = Union[OrderedPair, Point2D]
PairOfPoints = Tuple[AnyPoint, AnyPoint]
