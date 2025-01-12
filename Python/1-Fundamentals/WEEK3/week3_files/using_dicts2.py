state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}

# print(len(state_capitals))
# dictionaries are not indexed by number, they are indexed by keys

print(state_capitals["Washington"])

state_capitals["Washington"] = "Aberdeen"
state_capitals["Minnesota"] = "St. Paul"
print(state_capitals)

del state_capitals["California"]
print(state_capitals)

state_capitals.pop("Oregon")
print(state_capitals)

# what is the difference between using del and pop? pop has a return value and we can assign it to a variable.
# we can't do that with del
