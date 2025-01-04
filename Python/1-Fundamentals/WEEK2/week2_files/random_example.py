import random

# returns a random number between 1-10(inclusive)
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# returns a random choice from an array of choices
pets = ["dog", "cat", "bird", "fish"]
random_pet = random.choice(pets)
print(f"Random pet: {random_pet}")


# given a list, will shuffle its order randomly
random.shuffle(pets)
print(f"Shuffled pets: {pets}")
