# class Player:
#     # class attribute
#     max_hp = 4000


# # object from a class
# player1 = Player()
# print(player1.max_hp)
# player2 = Player()
# print(player2.max_hp)

# # class attributes and instance attributes

# #objects automatically changed to the value of the class attributes
# Player.max_hp = 5000
# print(player1.max_hp)
# print(player2.max_hp)

# instance attributes are stored per instance, rather than on the class

class Player:
    # constructor method
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)
# self is handled by python itself so we don't pass it in

print("P1: ", player1.name, "--HP: ", player1.hp)
print("P2:", player2.name, " --HP: ", player2.hp)

player1.hp += 500
player1.score += 10
print("p1 hp equals", player1.hp)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # defined inside the class so it is a method
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)
user1.change_password("bestpassword")

# class inheritance: a new class can be defined by extending an existing class.
# Existing class: parent class or super class
# new class: child class or subclass

# class Parent:
#     def __init__():
#     #parent methods and attributes are defined here

# class Child(Parent):
#     #parent methods and attributes are inherited
#     #child methods and attributes are defined here


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, direction):
        print(self.name, "walks to the", direction)

    def talk(self, speech):
        print(self.name, "says", speech)

# wizard class is a sub class of Human


class Wizard(Human):
    def cast_spell(self, spell):
        print(self.name, "casts", spell)


# super function

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, direction):
        print(self.name, "walks to the", direction)

    def talk(self, speech):
        print(self.name, "says", speech)


class Wizard(Human):
    def __init__(self, name, age, spell_points):
        super().__init__(name, age)
        self.spell_points = spell_points

    def cast_spell(self, spell):
        print(self.name, "casts", spell)
