def linear_search_dictionary(my_dictionary, target):
    for key, value in my_dictionary.items():
        if value == target:
            print(f"Success! You found the target! The key is: {key}")
            return key

    print("Whoops. You did not find the target")
    return None


# Example dictionary
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}

# Searching for various targets
linear_search_dictionary(my_dictionary, 5)  # Target found (red)
linear_search_dictionary(my_dictionary, 3)  # Target found (blue)
linear_search_dictionary(my_dictionary, 8)  # Target not found
