from dataclasses import dataclass

@dataclass
class Point2D:
    x: float
    y: float

    def __repr__(self):
        return f'Point2D<{self.x},{self.y}>'
