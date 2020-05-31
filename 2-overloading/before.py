"""
Goal:
Define a Circle class which does nothing but storing a radius.
It should be initialisable with either a radius or a circumference.
"""

import math
from typing import Optional


class Circle:
    radius: float

    # Note the use of 'keyword-only' arguments (arguments after *)
    # This means users must use the keyword radius= or circumference= when calling.
    # Otherwise there'd be no clear way to tell which they meant.
    def __init__(
        self, *, radius: Optional[float] = None, circumference: Optional[float] = None
    ):
        if radius is not None and circumference is not None:
            raise ValueError("Cannot use both radius and circumference")

        if radius is not None:
            self.radius = radius
        elif circumference is not None:
            self.radius = circumference / math.tau
        else:
            raise ValueError("Must give either a radius or circumference")


# Valid things (are they all allowed by mypy?)
Circle(radius=1.0)
Circle(circumference=math.tau)

# Invalid things (are they all caught by mypy?)
Circle(radius=None)
Circle(circumference=None)
Circle(radius=1.0, circumference=None)
Circle(radius=1.0, circumference=3.0)
