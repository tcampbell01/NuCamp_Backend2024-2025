class Vehicle:
    def __init__(self, num_wheels, color):
        self.num_wheels = num_wheels
        self.color = color
        self.fuel_percent = 0

    def add_fuel(self, fuel_amt):
        self.fuel_percent += fuel_amt


motorcycle = Vehicle(2, "black")

motorcycle.add_fuel(100)


print("Your fuel percentage is: ", motorcycle.fuel_percent)

# class inheritance


class Truck(Vehicle):
    def __init__(self, num_wheels, color):
        super().__init__(num_wheels, color)

# Linked Lists do not exist natively in Python
# More efficient at inserting and deleting data because the index does not need to be shifted

# Head node is first, tail node is last
# Each item ("node") in a linked list has reference to the next node
# Traverse entire linked list by going from one node to the next
# For tail node, the next node has a null value (such as Python's None value)
