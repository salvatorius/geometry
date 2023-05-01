from geometry import PointList, Point2D, is_valid_point_set

class Line:

    UNDEFINED = None

    def __init__(self, *points: PointList, gradient: float = None, y_intercept: float = None):
        self._gradient = gradient
        self._intercept = y_intercept
        init_points = list(points) if points else []
        if init_points and not is_valid_point_set(init_points, min_len=1, max_len=2):
            raise ValueError("Wrong set of Points")
        # Whenever both y_intercept and the single point are available
        if y_intercept and init_points and len(init_points) < 2:
            # prepare to use the logic for two points
            init_points += Point2D(0, y_intercept)
        # Given 2 points ∴ Calculate gradient and y-axis intercept
        if init_points and is_valid_point_set(init_points, min_len=2):
            (x1, y1), (x2, y2) = init_points
            if x2 == x1:
                self._gradient = Line.UNDEFINED
            else:
                self._gradient = (y2 - y1) / (x2 - x1)
                self._intercept = y1 - self._gradient * x1

    @property
    def gradient(self):
        return self._gradient

    @property
    def intercept(self):
        return self._intercept

    def __and__(self, other) -> Point2D:
        pass
