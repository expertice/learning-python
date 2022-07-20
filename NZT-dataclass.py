
"""
class Human(object):
    def __init__(self, firstname, lastname, age, year):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.year = year

human = Human("Boris", "Johnson", 100, 1922)
"""
from dataclasses import dataclass, field


@dataclass  # (frozen=True) can't modify an object
class Human(object):
    firstname: str = "Ivanov"
    lastname: str = "Ivan"
    age: int = 17
    year: int = 2014
    fullname: str = field(init=False, repr=False)

    def __post_init__(self):
        self.fullname = f"{self.firstname} {self.lastname}"

@dataclass
class Additional(object):
    growth: int = 185
    weight: int = 80

@dataclass
class Data:
    human: Human
    additional: Additional

def get_data():
    data = Data(
        human=Human("Peter", "Pyatochkin", 20, 2002),
        additional=Additional(150, 100)
    )
    return data

"""human = Human("Boris", "Johnson", 100, 1922)
human1 = Human()
print(human1)
print(human.fullname)"""

get_values = get_data()
print(get_values)
