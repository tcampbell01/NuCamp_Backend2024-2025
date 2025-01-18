OOP:
class based approach

objects are instances of a class
many objects can be made from the same class

- can think of classes as a data type/data structure that we create rather than one that is built into python

class inheritance: child classes can be based on parent classes

- usually more complex classes from simpler classes, share base code

example:
Parent class: House
Child classes: cottage, mansion, etc, all inherit from house class

in OOP: classes are used as templates for objects

- Objects are instantiated form classes (thus also called instances)
- classes/objects have attributes and methods
  \*attributes and methods are like variables and functins, attached to specific classes/objects

attributes are like nouns, methods are like verbs \*\*\*\*

class ClassName:
def **init**(self, attr1, attr2...):

        self.attr1 = ...
        self.attr2 = ...

    def method1(self, ...)

example:

class Vehicle:
def **init**(self, num_wheels, color):
self.num_wheels = num_wheels
self.color = color
self.fuel_percentage = 0

    def add_fuel(self, fuel_amt):
        self.fuel_percentage += fuel_amt

    is a default attribute always 0?

    #how to create an instance of this class with the name of "motorcycle" and a color of "black"

    #these attributes were taken from the attributes of the Vehicle class
    motorcycle =(2, "black")
        self.fuel +
