# If you can't use Python 3.8, you can also import Protocol from typing-extensions
# https://pypi.org/project/typing-extensions/
from typing import Protocol
from dataclasses import dataclass


@dataclass
class Dog:
    name: str
    color: str


@dataclass
class Company:
    name: str
    address: str


class Human:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height


class NamedThing(Protocol):
    """
    With Protocols, any type that has the indicated properties and methods
    will be recognised as conforming to this Protocol, even without that type
    explicitly inheriting from the Protocol.

    Notice that Dog, Company and Human have not inherited from NamedThing.
    """
    name: str


def say_name(named_thing: NamedThing) -> None:
    print(f"This thing is named: {named_thing.name}")


# Valid things (are they all allowed by mypy?)
say_name(Dog(name="spots", color="white"))
say_name(Company(name="Five AI", address="20 Cambridge Place"))
say_name(Human(name="LeBron James", height=2.06))

# Invalid things (are they all caught by mypy?)
say_name(42)
say_name("blah")
