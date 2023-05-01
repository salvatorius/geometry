from dataclasses import dataclass
from typing import List, Tuple, Union, Any

Numeric = Union[float, int]

@dataclass
class BasePair:
    x: Numeric
    y: Numeric

    def __getitem__(self, key):
        if not key in (0,1):
            raise ValueError("Only 2 indices available: 0,1 for x,y")
        return self.x if key == 0 else self.y

OrderedPair = Union[Tuple[Numeric,Numeric],BasePair]
OrdererPairOrList = Union[OrderedPair,List[Numeric]]

def is_numeric(subject: Union[Any,Numeric]) -> bool:
    return isinstance(subject, (int, float)) \
        and not isinstance(subject, bool)

def has_numeric_values(subject: Any, up_to=None) -> bool:
    return isinstance(subject, (list, tuple)) \
        and all(map(is_numeric, subject[:up_to])) \
            or issubclass(type(subject), BasePair)

class Point2D(BasePair):
    def __new__(cls, *args: OrdererPairOrList):
        is_single=False
        if not args or args[0] is None:
            raise ValueError("Missing Arguments (coordinates)")
        if has_numeric_values(args[0], up_to=2):
            is_single=True
        elif not has_numeric_values(args, up_to=2):
            raise TypeError(f"Expected Point or tuple/list of 2 floats, got {type(args)} : {args=}")
        instanced = super().__new__(cls)
        instanced.__is_single = is_single
        return instanced

    def __init__(self, *args: OrdererPairOrList):
        left, pair = args[0], args[:2]
        if self.__is_single:
            pair = left
        elif len(pair) == 1:
            pair = (0, left)
        super().__init__(pair[0], pair[1])

    def __repr__(self):
        return f'Point2D [{self.x},{self.y}]'

    @property
    def tuple(self) -> OrderedPair:
        return tuple((self.x, self.y))

AnyPoint = Union[OrderedPair, Point2D]
PointList = Union[Tuple[AnyPoint, ...], List[AnyPoint]]

def is_valid_point(obj: AnyPoint) -> bool:
    return isinstance(obj, Point2D) \
        or isinstance(obj, (tuple, list)) and len(obj) == 2 \
            and all(isinstance(v, (int, float)) for v in obj)

def is_valid_point_set(obj: PointList, *, min_len: int = None, max_len: int = None) -> bool:
    return isinstance(obj, (tuple, list)) \
        and (not min_len or len(obj) >= min_len) \
        and (not max_len or len(obj) <= max_len) \
        and all(is_valid_point(p) for p in obj)

def is_valid_pair_of_points(obj: PointList) -> bool:
    return is_valid_point_set(obj, min_len=2, max_len=2)
