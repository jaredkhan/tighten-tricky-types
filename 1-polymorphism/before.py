"""
Goal:
Define a function which takes any value and a number `n`
and returns a list of that value repeated `n` times.
"""

from typing import Any, List


def repeat(value: Any, times: int) -> List[Any]:
    return [value] * times


# Valid things (are they all allowed by mypy?)
my_int = repeat(0, 100)[0] - 12
my_text = repeat("hello", 100)[0] + " world"

# Invalid things (are they all caught by mypy?)
bad_int = repeat(0, 100)[0] + " words"  # Trying to add a number and a string
