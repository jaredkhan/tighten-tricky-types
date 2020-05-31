# Top tips to tighten tricky types

Python type checkers help us catch bugs earlier. The more specific we can make our type annotations, the more bugs the type checker can catch.

In this repository, we have a few examples of how to make your function signatures more specific in Python.

Each example has some function, with a 'before' and an 'after'.
The implementation of the function won't change between the before and after, but the type annotations will.

You can run `mypy` (or your favourite Python type-checker) on the examples to see that being more specific about our types 
can prevent invalid usages of functions before the code is even run.

To check the examples:
```bash
virtualenv venv -p python3.8
source venv/bin/activate
pip install mypy
mypy 1-polymorphism/before.py
mypy 1-polymorphism/after.py
mypy 2-overloading/before.py
...
```

### Quick Summary
Here's a peek at what the examples will show:
1. Polymorphism with `TypeVar`
    
    Describe relationships between input and output types
    ```
    T = TypeVar('T')
    
    def repeat(value: T, times: int) -> List[T]:
        return [value] * times
    ```
2. Overloading with `@overload`

    Describe the multiple valid combinations of inputs to your function
    ```
    @overload
    def draw_circle(*, radius: float): ...

    @overload
    def draw_circle(*, circumference: float): ...

    def draw_circle(*, radius: Optional[float] = None, circumference: Optional[float] = None):
        # Implementation goes here
    ```
3. Static duck-typing with `Protocol`
    
    Check that inputs have certain properties or methods,
    without having them explicitly inherit from any class.
    ```
    @dataclass
    class Dog:
        name: str
        color: str
    
    
    class NamedThing(Protocol):
        name: str
    
    
    def say_name(named_thing: NamedThing) -> None:
        print(f"This thing is named: {named_thing.name}")
    
    
    say_name(Dog(name="spots", color="white"))
    ```


