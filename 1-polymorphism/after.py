from typing import TypeVar, List

T = TypeVar('T')


# For each usage of `repeat`,
# the type checker will now know that the elements of the output list have the same type as `value`.
def repeat(value: T, times: int) -> List[T]:
    return [value] * times


# Valid things
my_int = repeat(0, 100)[0] - 12
my_text = repeat("hello", 100)[0] + " world"

# Invalid things
bad_int = repeat(0, 100)[0] + " words"
