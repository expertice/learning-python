# :TODO: need new names for class variables
class Basket(object):
    busy_space = 0

    def __init__(self, size_of_crate):
        self.crate_dimension = size_of_crate
        print(f"Created new Basket with {size_of_crate} cells")

    def loading_item(self, new_item_dimension):
        if self.crate_dimension - new_item_dimension >= 0:
            print(f"Loading item with {new_item_dimension} dimension")
            self.busy_space += new_item_dimension
            print(f"There are {self.crate_dimension - self.busy_space} free cells left")
        else:
            print(f"Can't put item with {new_item_dimension} in, "
                  f"cause only {self.crate_dimension - self.busy_space} free space left")
        return self.busy_space


class Bag(Basket):
    def __init__(self, size_of_bag):
        self.crate_dimension = size_of_bag
        print(f"Created new Bag with {size_of_bag} cells")


class Item(object):
    # :TODO: describe a new class to put objects in Basket or Bag
    pass


b1 = Basket(15)
b1.loading_item(5)
# b1.loading_item(8)
# b1.loading_item(21)
bag1 = Bag(7)
bag1.loading_item(6)
b1.loading_item(bag1.crate_dimension)
