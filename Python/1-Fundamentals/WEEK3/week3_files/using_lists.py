states = ["Washington", "Oregon", "California"]

print(states[0])
print(states[1])
print(states[2])

# access the last item in the list
'''
print(states[-1])
print(states[-2])
print(states[-3])

'''

states[2] = "Arizona"
# print(states)

# how many items are in a list
# print(len(states))

# what is the difference between a function and a method?
# Unlike functions, methods are always associated with objects
# A list is a type of object

states.append("New York")
print(states)

# .pop without an argument will remove the last item from the list
states.pop()
print(states)

states.pop(1)
print(states)
