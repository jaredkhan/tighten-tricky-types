"""
Goal:
Define a function which takes any value and a number `n`
and returns a list of that value repeated `n` times.
"""

from typing import Any, List


def repeat(value: Any, times: int) -> List[Any]:
    return [value] * times


# Valid things
my_int = repeat(0, 100)[0] - 12
my_text = repeat("hello", 100)[0] + " world"

# Invalid things
bad_int = repeat(0, 100)[0] + " words"
