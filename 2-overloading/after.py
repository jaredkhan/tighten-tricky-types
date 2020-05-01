import math
from typing import overload, Optional


class Circle:
    radius: float

    @overload
    def __init__(self, *, radius: float): ...

    @overload
    def __init__(self, *, circumference: float): ...

    def __init__(self, *, radius: Optional[float] = None, circumference: Optional[float] = None):
        if radius is None and circumference is None:
            raise ValueError("Cannot use both radius and circumference")

        if radius is not None:
            self.radius = radius
        elif circumference is not None:
            self.radius = circumference / math.tau
        else:
            raise ValueError("Must give either a radius or circumference")


# Valid thing
Circle(radius=1.0)
Circle(circumference=math.tau)

# Invalid things
Circle(radius=None)
Circle(circumference=None)
Circle(radius=1.0, circumference=None)
Circle(radius=1.0, circumference=3.0)


