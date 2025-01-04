import random

nouns = []
verbs = []
adjectives = []
plural_nouns = []

# will use input to collect a number of nouns.  After each input, the noun will be added to an array.


def collect_nouns():
    # use a for loop to collect nouns
    noun_collection = input(
        "Please enter a noun followed by 'enter'. When you are satisfied with your noun list, press 1")
    nouns.append(noun_collection)
    print(f"Your updated list is: {nouns}")
    # press 1 when you are finished

# will use input to collect a number of verbs.  After each input, the verbs will be added to an array.


def collect_verbs():
    # use a for loop to collect verbs
    verb_collection = input(
        "Please enter a verb followed by 'enter'. When you are satisfied with your verb list, press 1")
    verbs.append(verb_collection)
    print(f"Your updated verb list is: {verbs}")
    # press 1 when you are finished

# will use input to collect a number of adjectives.  After each input, the adjectives will be added to an array.


def collect_adjectives():
    adjective_collection = input(
        "Please enter an adjective followed by 'enter'. When you are satisfied with your adjective list, press 1")
    adjectives.append(adjective_collection)
    print(f"Your updated list is: {adjectives}")


# will use input to collect a number of plural nouns.  After each input, the plural nouns will be added to an array.
def collect_plural_nouns():
    # use a for loop to collect plural nouns
    plural_noun_collection = input(
        "Please enter a plural noun followed by 'enter'. When you are satisfied with your plural noun list, press 1")
    plural_nouns.append(plural_noun_collection)
    print(f"Your updated plural noun collection is: {plural_nouns}")


# print the story to the console while calling a random.choice from the array list
def tell_story():
    random.choice(verbs)
    random.choice(nouns)
    random.choice(adjectives)
    random.choice(plural_nouns)
