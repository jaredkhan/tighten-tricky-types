from typing import TypeVar, List

T = TypeVar('T')  # The string in this constructor is just for type checker error messages


def repeat(value: T, times: int) -> List[T]:
    """
    For each usage of `repeat`, the type checker will now
    know that the elements of the output list have the same
    type as `value` thanks to the usage of the TypeVar T in
    both the input types and the output type.
    """
    return [value] * times


# Valid things (are they all allowed by mypy?)
my_int = repeat(0, 100)[0] - 12
my_text = repeat("hello", 100)[0] + " world"

# Invalid things (are they all caught by mypy?)
bad_int = repeat(0, 100)[0] + " words"
