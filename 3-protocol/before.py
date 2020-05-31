"""
Goal:
Define a function which can take any object with a 'name' attribute
and print that name.
"""

from typing import Any, Union
from dataclasses import dataclass


@dataclass
class Dog:
    name: str
    color: str


@dataclass
class Company:
    name: str
    address: str


@dataclass
class Human:
    name: str
    height: float


def say_name(named_thing: Any) -> None:
    print(f"This thing is named: {named_thing.name}")


def say_name_again(named_thing: Union[Dog, Company]) -> None:
    """
    A second attampt: we might also try to accept a Union of the types that we expect.
    """
    print(f"This thing is named: {named_thing.name}")


# Valid things (are they all allowed by mypy?)
say_name(Dog(name="spots", color="white"))
say_name(Company(name="Five AI", address="20 Cambridge Place"))
say_name(Human(name="LeBron James", height=2.06))

say_name_again(Dog(name="spots", color="white"))
say_name_again(Company(name="Five AI", address="20 Cambridge Place"))
say_name_again(Human(name="LeBron James", height=2.06))

# Invalid things (are they all caught by mypy?)
say_name(42)
say_name("blah")

say_name_again(42)
say_name_again("blah")
