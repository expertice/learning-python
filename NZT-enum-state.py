from enum import Enum

class StateHuman(Enum):
    smoking = (1, "курит", "vape")
    sits = (2, "сидит", "sofa")
    drink = (3, "пьёт", "juice")

    def __init__(self, id, description, check):
        self.id = id
        self.description = description
        self.check = check


class Human(object):
    def __init__(self, state: StateHuman, name, age):
        self.state = state
        self.name = name
        self.age = age

"""
for state in StateHuman:
    print(f"{state.value} {state.id}")
    for position in state.value:
        print(position)

print(StateHuman.sits.name, StateHuman.sits.value)
"""

human = Human(StateHuman.smoking, "Boris", 45)
print(human.state.value)
print(human.state.id)