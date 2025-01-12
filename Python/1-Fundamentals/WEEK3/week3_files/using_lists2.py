states = ["Washington", "Oregon", "California"]

"""
for state in states:
    state = state.lower()
    print(state)

"""

"""
print("Washington" in states)  # returns True
print("Minnesota" in states)  # returns False
print("Washington" not in states)  # returns False

"""

states2 = ["Minnesota", "Connecticut", "New York"]
best_states = states + states2
print(best_states)

print(best_states[1:3])  # starting at 1, up to but not including 3
print(best_states[:2])  # starting at 0, up to but not including 2
print(best_states[4:])  # starting at 4 to the end


# ['Washington', 'Oregon', 'California', 'Minnesota', 'Connecticut', 'New York']
print(best_states)
print(best_states[-3:-1])  # ['Minnesota', 'Connecticut']
print(best_states[:-2])  # ['Washington', 'Oregon', 'California', 'Minnesota']
print(best_states[-1:])  # ['New York']
