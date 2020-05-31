import math
from typing import overload, Optional

"""
Overloading in Python is different to other languages.

In other languages, we might give multiple implementations of a single function
and the correct one will be chosen based on the given input types.

In Python, we are *not* going to define multiple implementations 
(remember our type annotations aren't read at runtime). 
In Python we just have one implementation, which *manually* checks the types and does the right thing.
All @overload lets us do is tell the *type checker* which combinations of parameters and outputs are valid.

We do this be providing multiple @overload signatures before defining our actual implementation.
The type checker will make sure that our implementation supports all the @overload signatures described.
"""


class Circle:
    radius: float

    # The implementation of overloads is immediately overwritten
    # by the main implementation, so doesn't matter what we put inside.
    # Here we use the `...` syntax

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


# Valid things (are they all allowed by mypy?)
Circle(radius=1.0)
Circle(circumference=math.tau)

# Invalid things (are they all caught by mypy?)
Circle(radius=None)
Circle(circumference=None)
Circle(radius=1.0, circumference=None)
Circle(radius=1.0, circumference=3.0)


