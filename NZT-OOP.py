class House(object):
    r_material = "Shingles"
    def __init__(self, floor):
        self.__square = 100
        self.floor = floor
        self.__wall = "wall"
        print(f"House is created with SQ= {self.__square}, FL = {self.floor} and WA = {self.__wall}")

    def build_balcony(self, b_square):
        self.square -= b_square
        print(f"Balcony added, SQ= {self.__square}, FL = {self.floor} and WA = {self.__wall}")

    def build_roof(self):
        print(f"Roof is created with material {self.r_material}")

    def info(self):
        print(f"House parameters: SQ: {self.__square}, FL: {self.floor}, WA: {self.__wall}, RF: {self.r_material}")

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, set_square):
        try:
            if set_square < 15:
                self.__square = 15
            elif set_square > 100:
                self.__square = 100
            else:
                self.__square = set_square
        except Exception as e:
            print ("Square must be numerical value")

    @property
    def wall(self):
        return self.__wall

    @wall.setter
    def wall(self, wall):
        self.__wall = wall


House.r_material = "Slate"
print(House.r_material)
house = House(5)
print (f"House square is {house.square}")
house.build_balcony(15)
print (f"House square is {house.square}")
house.build_roof()
# house.set_wall("bricks")
house.wall = "Plate"
print(f"House wall is from {house.wall}")

house.square = 'very big'
house.info()

print(f"Getting secret value {house._House__square}")