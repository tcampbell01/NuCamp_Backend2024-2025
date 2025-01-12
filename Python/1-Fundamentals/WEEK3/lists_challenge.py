import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    pick_up_cards = input("Push enter to pick up a card or Q to quit: ")
    if pick_up_cards == "Q":
        break
    else:
        random_card_number = random.randrange(0, len(diamonds))
        print(f"""Your random number is: {random_card_number}""")

        random_card = diamonds.pop(random_card_number)
        print(f"""Your random card is: {random_card}""")
        hand.append(random_card)
        print(f"""The diamonds that are left are: {diamonds}""")
        print(f"""Your current hand is: {hand}""")

        if not diamonds:
            print("There are no more cards to pick")
