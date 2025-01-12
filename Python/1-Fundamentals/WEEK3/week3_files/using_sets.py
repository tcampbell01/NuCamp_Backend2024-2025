numbers_set = {1, 2, 3, 4, 4}

# removes duplicates
print(numbers_set)

# sets cannot use mutable data types and cannot be accessed by an index.
# must iterate through the set to access the parts inside the set

words_set = {"Alpha", "Bravo", "Charlie"}

abcd = ""

# sets are unordered
for word in words_set:

    abcd += word
print(abcd)

if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha is not in set")

words_set.add("Delta")
print(words_set)

words_set.discard("Bravo")
print(words_set)
