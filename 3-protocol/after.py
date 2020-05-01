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


@dataclass
class Human:
    name: str
    height: float


class NamedThing(Protocol):
    name: str


def say_name(named_thing: NamedThing) -> None:
    print(f"This thing is named: {named_thing.name}")


# Valid things
say_name(Dog(name="spots", color="white"))
say_name(Company(name="Five AI", address="20 Cambridge Place"))
say_name(Human(name="LeBron James", height=2.06))

# Invalid things
say_name(42)
say_name("blah")
