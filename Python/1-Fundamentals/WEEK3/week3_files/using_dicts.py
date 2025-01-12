state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}

# prints the key of each pair
for state in state_capitals:
    print(state)

# iterate using values
for city in state_capitals.values():
    print(city)

# access both keys and values
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

# another way to access both keys and values
for state, city in state_capitals.items():
    print(city, "is the capital of", state)
