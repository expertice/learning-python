from enum import Enum

class Days(Enum):
    Monday = (1, "Понедельник")
    Tuesday = (2, "Вторник")
    Wednesday = (3, "Среда")
    Thursday = (4, "Четверг")
    Friday = (5, "Пятница")
    Saturday = (6, "Суббота")
    Sunday = (7, "Воскресенье")

    def __init__(self, id, russian):
        self.id = id
        self.russian = russian

class Seasons(Enum):
    Winter = ["December", "January", "February", ]
    Spring = ["March", "April", "May", ]
    Summer = ["June", "July", "August", ]
    Autumn = ["September", "October", "November", ]

for season in Seasons:
    print(f"Season is {season.name}, {season}")
    for month in season.value:
        print(f"Month is {month}")


"""
for day in Days:
    print(f"{day.name} - это {day.id}-й день недели, по-русски '{day.russian}'")
"""