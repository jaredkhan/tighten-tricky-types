"""
Goal:
Define a function which can take any object with a 'name' attribute
and print that name.
"""

from typing import Any
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

# A second attempt:

# def say_name(named_thing: Union[Dog, Company]) -> None:
#     print(f"This thing is named: {named_thing.name}")


# Valid things
say_name(Dog(name="spots", color="white"))
say_name(Company(name="Five AI", address="20 Cambridge Place"))
say_name(Human(name="LeBron James", height=2.06))

# Invalid things
say_name(42)
say_name("blah")
