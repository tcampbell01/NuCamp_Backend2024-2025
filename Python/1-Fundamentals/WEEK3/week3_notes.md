inbuilt datastructures in python:

4 non-primitive inbuilt data structures: Lists, Dictionary, Tuple, and Set

Lists: Lists in python are one of the most versatile collection object types available.

- Python lists do the work of most of the collection data structures found in other languages and since they are built in, you don't have to worry about manually creating them.
- Lists can be used for any type of object, from numbers and strings to more lists
- They are accessed just like strings(ex. slicing and concatenation) so they are simple to use and they're variable length(i.e they grow and shrink automatically as they're used)
- In reality, Python lists are C arrays inside the Python interpreter and act like an array of pointers

Dictionaries: In python, dictionary is similar to hash or maps in other languages. It consists of key value pairs. The value can be accessed by unique key in the dictionary.

- Keys are unique and immutable objects
- Syntax: dictionary = {"key name": value}

Tuple: Python tuples work exactly like Python lists except they are immutable. (ie they can't be changed in place). They are normally written inside parentheses to distinguish them from lists(which use square brackets), but as you'll see, parentheses aren't always necessary. Since tuples are immutable, their length is fixed. To grow or shrink a tuple, a new tuple must be created.

() An empty tuple
t1 = (0, ) A one-item tuple (not an expression)
t2 = (0, 1, 2, 3) A four-item tuple
t3 = 0, 1, 2, 3 Another four-item tuple (same as prior line, just minus the parenthesis)
t3 = (‘abc’, (‘def’, ‘ghi’)) Nested tuples
t1[n], t3[n][j] Index
t1[i:j], Slice
len(tl) Length

# Python program to illustrate

# tuple

tup = (1, "a", "string", 1+2)
print (tup)
print (tup[1])
